from bs4 import BeautifulSoup
import requests
import json
import logging
import certifi  # Added for SSL certificate validation
from urllib.parse import urljoin
from datetime import datetime
import os  # For checking if the model file exists
import joblib  # For loading the model
import time
from requests.exceptions import Timeout, ConnectionError
from train_model import train_model  # import it at the top of scanner.py


class WebScanner:
    def __init__(self, url, scan_type, payloads):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.results = []
        self.session = requests.Session()

        # Check if the model file exists, only load it if exists
        if os.path.exists('vulnerability_model.pkl'):
            self.model = joblib.load('vulnerability_model.pkl')
            print("[+] AI model loaded successfully.")
        else:
            self.model = None
            print("[!] No AI model found. Skipping AI-based predictions.")

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
            retries = 3
            for i in range(retries):
                try:
                    response = self.session.get(url, params={"q": payload}, timeout=15, verify=certifi.where())
                    if payload in response.text or 'error' in response.text.lower():
                        self.log_vulnerability(url, payload)
                    break  # Exit the retry loop if successful
                except (Timeout, ConnectionError) as e:
                    print(f"[!] Error: {e} - Retry {i+1}/{retries}")
                    if i == retries - 1:
                        print(f"[!] Failed to access {url} after {retries} attempts.")
                        time.sleep(5)  # Wait 5 seconds before retrying

            # Parse the HTML content into BeautifulSoup after the request
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for form elements in the page
            for form in soup.find_all("form"):
                action = urljoin(url, form.get("action", ""))
                method = form.get("method", "get").lower()
                inputs = form.find_all("input")

                for payload in self.payloads:
                    # Prepare form data
                    data = {i.get("name"): payload for i in inputs if i.get("name")}
                    try:
                        # Send POST or GET request based on form method
                        if method == "post":
                            response = self.session.post(action, data=data, timeout=5, verify=certifi.where())
                        else:
                            response = self.session.get(action, params=data, timeout=5, verify=certifi.where())

                        # Check for vulnerability based on payload
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

    # 🔁 Auto-retrain AI model with new data
        print("[*] Retraining AI model with latest scan data...")
        train_model()