import requests
import json
import logging
import certifi
from urllib.parse import urljoin
from datetime import datetime
import os
import joblib
from train_model import train_model
import concurrent.futures

class WebScanner:
    def __init__(self, url, scan_type, payloads):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.results = []
        self.session = requests.Session()

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
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(self._scan_single_url, url, item) for item in self.payloads]
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def _scan_single_url(self, url, item):

        try:
            payload = item["payload"]
            risk = item.get("risk", "unknown")
            response = self.session.get(url, params={"q": payload}, timeout=30, verify=certifi.where())

            if payload in response.text or 'error' in response.text.lower():
                self.log_vulnerability(url, payload, risk)
        except requests.exceptions.RequestException as e:
             logging.info(f"[IGNORED] Could not access {url}: {e}")


    def scan_sensitive_files(self):
        for item in self.payloads:
            file_path = item["payload"]
            risk = item.get("risk", "unknown")
            target = urljoin(self.url, file_path)
            try:
                response = self.session.get(target, timeout=30, verify=certifi.where())
                if response.status_code == 200:
                    self.log_vulnerability(target, file_path, risk)
            except Exception as e:
                logging.error(f"Failed to check {target} - {e}")

    def log_vulnerability(self, url, payload, risk):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "url": url,
            "vulnerability": self.scan_type,
            "payload": payload,
            "risk": risk
        }
        self.results.append(entry)
        logging.warning(f"[VULNERABILITY] {entry}")

    def save_report(self):
        with open("scan_report.json", "w") as f:
            json.dump({"vulnerabilities": self.results}, f, indent=4)
        print("[+] Report saved to scan_report.json")

        print("[*] Retraining AI model with latest scan data...")
        train_model(filter_type=self.scan_type) 