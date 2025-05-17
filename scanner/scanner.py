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
from scanner.utils import extract_forms

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
        try:
            response = self.session.get(url, timeout=30, verify=certifi.where())
            html = response.text

            # Scan forms
            forms = extract_forms(html)
            for form in forms:
                form_details = self.get_form_details(form)
                for item in self.payloads:
                    self.submit_form(form_details, url, item)

            # Scan URL directly with payloads
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                futures = [executor.submit(self._scan_single_url, url, item) for item in self.payloads]
                for future in concurrent.futures.as_completed(futures):
                    future.result()

        except requests.exceptions.RequestException as e:
            logging.info(f"[IGNORED] Could not access {url}: {e}")

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

    def get_form_details(self, form):
        action = form.get("action")
        method = form.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.get("type", "text").lower()
            name = input_tag.get("name")
            value = input_tag.get("value", "")
            if name:
                inputs.append({"type": input_type, "name": name, "value": value})

        for textarea in form.find_all("textarea"):
            name = textarea.get("name")
            value = textarea.text
            if name:
                inputs.append({"type": "textarea", "name": name, "value": value})

        for select in form.find_all("select"):
            name = select.get("name")
            value = None
            selected_option = select.find("option", selected=True)
            if selected_option:
                value = selected_option.get("value")
            else:
                first_option = select.find("option")
                if first_option:
                    value = first_option.get("value")
            if name:
                inputs.append({"type": "select", "name": name, "value": value})

        return {"action": action, "method": method, "inputs": inputs}

    def submit_form(self, form_details, base_url, item):
        payload = item["payload"]
        risk = item.get("risk", "unknown")
        target_url = urljoin(base_url, form_details["action"])
        data = {}

        for input_field in form_details["inputs"]:
            field_type = input_field["type"]
            name = input_field["name"]

            if not name:
                continue

            if field_type in ["text", "search", "email", "textarea"]:
                data[name] = payload
            elif field_type in ["checkbox", "radio"]:
                data[name] = input_field["value"] if input_field["value"] else payload
            else:
                data[name] = input_field["value"]

        try:
            if form_details["method"] == "post":
                response = self.session.post(target_url, data=data, timeout=30, verify=certifi.where())
            else:
                response = self.session.get(target_url, params=data, timeout=30, verify=certifi.where())

            if payload in response.text:
                self.log_vulnerability(target_url, payload, risk)
        except Exception as e:
            logging.error(f"Form submission failed to {target_url} - {e}")

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
