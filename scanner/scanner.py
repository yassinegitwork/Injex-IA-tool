# scanner.py
import requests
import json
import logging
import certifi  # Added for SSL certificate validation
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

class WebScanner:
    def __init__(self, url, scan_type, payloads):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.results = []
        self.session = requests.Session()

        logging.basicConfig(filename="scan_log.txt", level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")

    def run_scan(self, urls):
        print(f"[+] Running {self.scan_type.upper()} scan on {len(urls)} discovered pages...")
        if self.scan_type == "sensitive":
            self.scan_sensitive_files()
        else:
            for url in urls:
                self.scan_url(url)
        self.save_report()

    def scan_url(self, url):
        for payload in self.payloads:
            try:
                response = self.session.get(url, params={"q": payload}, timeout=5, verify=certifi.where())  # Using certifi for verification
                if payload in response.text or 'error' in response.text.lower():
                    self.log_vulnerability(url, payload)
            except Exception as e:
                logging.error(f"Failed to scan {url} - {e}")

        response = self.session.get(url, timeout=5, verify=certifi.where())  # Using certifi for verification
        soup = BeautifulSoup(response.text, "html.parser")

        for form in soup.find_all("form"):
            action = urljoin(url, form.get("action", ""))
            method = form.get("method", "get").lower()
            inputs = form.find_all("input")

            for payload in self.payloads:
                data = {i.get("name"): payload for i in inputs if i.get("name")}
                try:
                    if method == "post":
                        response = self.session.post(action, data=data, timeout=5, verify=certifi.where())  # Using certifi for verification
                    else:
                        response = self.session.get(action, params=data, timeout=5, verify=certifi.where())  # Using certifi for verification
                    if payload in response.text or 'error' in response.text.lower():
                        self.log_vulnerability(action, payload)
                except Exception as e:
                    logging.error(f"Form scan failed at {action} - {e}")

    def scan_sensitive_files(self):
        for file_path in self.payloads:
            target = urljoin(self.url, file_path)
            try:
                response = self.session.get(target, timeout=5, verify=certifi.where())  # Using certifi for verification
                if response.status_code == 200:
                    self.log_vulnerability(target, "Sensitive File Found")
            except Exception as e:
                logging.error(f"Failed to check {target} - {e}")

    def log_vulnerability(self, url, payload):
        timestamp = datetime.now().isoformat()
        entry = {"timestamp": timestamp, "url": url, "vulnerability": self.scan_type, "payload": payload}
        self.results.append(entry)
        logging.warning(f"[VULNERABILITY] {entry}")

    def save_report(self):
        with open("scan_report.json", "w") as f:
            json.dump({"vulnerabilities": self.results}, f, indent=4)
        print("[+] Report saved to scan_report.json")
