import requests
import json
import logging
import certifi  # For SSL certificate validation
from urllib.parse import urljoin
from datetime import datetime
import os  # For checking if the model file exists
import joblib  # For loading the model
import time
from requests.exceptions import Timeout, ConnectionError
from train_model import train_model  # import it at the top of scanner.py
from bs4 import BeautifulSoup
import concurrent.futures  # For concurrent requests

class WebScanner:
    def __init__(self, url, scan_type, payloads, risk_levels):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.risk_levels = risk_levels
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
                self.scan_url(url)  # Uses the optimized scan_url
        self.save_report()

    def scan_url(self, url):
        # Start concurrent scanning for each payload
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(self._scan_single_url, url, payload) for payload in self.payloads]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # Wait for each task to finish

    def _scan_single_url(self, url, payload):
        try:
            response = self.session.get(url, params={"q": payload}, timeout=5, verify=certifi.where())  # Reduced timeout
            if payload in response.text or 'error' in response.text.lower():
                self.log_vulnerability(url, payload, self.risk_levels[self.payloads.index(payload)])
        except requests.exceptions.Timeout:
            print(f"Request to {url} timed out. Skipping.")
        except requests.exceptions.RequestException as e:
            print(f"Error during request to {url}: {e}")

    def scan_sensitive_files(self):
        for file_path in self.payloads:
            target = urljoin(self.url, file_path)
            try:
                response = self.session.get(target, timeout=5, verify=certifi.where())  # Using certifi for verification
                if response.status_code == 200:
                    self.log_vulnerability(target, "Sensitive File Found", "High")
            except Exception as e:
                logging.error(f"Failed to check {target} - {e}")

    def log_vulnerability(self, url, payload, risk):
        timestamp = datetime.now().isoformat()

        entry = {
            "timestamp": timestamp,
            "url": url,
            "vulnerability": self.scan_type,
            "payload": payload,
            "risk": risk  # Use the corresponding risk level
        }

        self.results.append(entry)
        logging.warning(f"[VULNERABILITY] {entry}")

    def save_report(self):
        with open("scan_report.json", "w") as f:
            json.dump({"vulnerabilities": self.results}, f, indent=4)
        print("[+] Report saved to scan_report.json")

        # 🔁 Auto-retrain AI model with new data
        print("[*] Retraining AI model with latest scan data...")
        train_model()

