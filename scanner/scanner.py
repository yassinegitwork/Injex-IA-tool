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
    def __init__(self, url, scan_type, payloads, risk_levels):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.risk_levels = risk_levels
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
            futures = [executor.submit(self._scan_single_url, url, payload) for payload in self.payloads]
            for future in concurrent.futures.as_completed(futures):
                future.result()

    def _scan_single_url(self, url, payload):
        try:
            response = self.session.get(url, params={"q": payload}, timeout=5, verify=certifi.where())
            if payload in response.text or 'error' in response.text.lower():
                risk = self.risk_levels[self.payloads.index(payload)] if self.payloads.index(payload) < len(self.risk_levels) else "unknown"
                self.log_vulnerability(url, payload, risk)
        except requests.exceptions.RequestException as e:
            print(f"Error during request to {url}: {e}")

    def scan_sensitive_files(self):
        for file_path in self.payloads:
            target = urljoin(self.url, file_path)
            try:
                response = self.session.get(target, timeout=5, verify=certifi.where())
                if response.status_code == 200:
                    print(f"[!] Sensitive file found: {target}")
                    self.log_vulnerability(target, file_path, "High")
            except Exception as e:
                logging.error(f"Failed to check {target} - {e}")

    def log_vulnerability(self, url, payload, risk=None):
        timestamp = datetime.now().isoformat()

        if risk is None:
            payload_data, risk_level = self._extract_payload_and_risk(payload)
        else:
            payload_data = payload
            risk_level = risk

        entry = {
            "timestamp": timestamp,
            "url": url,
            "vulnerability": self.scan_type,
            "payload": payload_data,
            "risk": risk_level
        }

        self.results.append(entry)
        logging.warning(f"[VULNERABILITY] {entry}")

    def _extract_payload_and_risk(self, payload):
        # Split payload and risk level based on the last comma (we assume risk is the last part)
        parts = payload.split(',', 1)
        if len(parts) == 2:
            return parts[0].strip(), parts[1].strip()  # Return the payload and risk level
        else:
            return payload, 'unknown'  # If no risk level is provided, return 'unknown'

    def save_report(self):
        with open("scan_report.json", "w") as f:
            json.dump({"vulnerabilities": self.results}, f, indent=4)
        print("[+] Report saved to scan_report.json")

        print("[*] Retraining AI model with latest scan data...")
        train_model()  # Retrain the model after the scan
