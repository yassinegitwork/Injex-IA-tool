import requests
import certifi
import re
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from scanner.payloads import XSS_PAYLOADS, SQLI_PAYLOADS

def is_valid_url(url):
    """ Validate and ensure the URL has the correct format """
    pattern = re.compile(
        r"^(https?:\/\/)?"  # Optional http/https
        r"([a-zA-Z0-9.-]+)"  # Domain name
        r"(\.[a-zA-Z]{2,})"  # Domain extension (.com, .net, etc.)
        r"(:\d{1,5})?"  # Optional port
        r"(\/.*)?$"  # Optional path
    )
    match = pattern.match(url)
    return bool(match)

def get_valid_url():
    """ Prompt the user for a valid URL and ensure it is correct """
    while True:
        user_url = input("[+] Please enter the target URL: ").strip()
        if not is_valid_url(user_url):
            print("❌ Invalid URL format. Please try again with a correct URL (http/https).")
        else:
            return user_url if user_url.startswith(('http://', 'https://')) else 'http://' + user_url

def get_scan_type():
    """ Prompt the user to choose the scan type (XSS or SQL Injection) """
    while True:
        scan_type = input("[+] Choose the scan type:\n[1] XSS Scan\n[2] SQL Injection Scan\nEnter 1 or 2: ").strip()
        if scan_type == "1":
            return "xss", XSS_PAYLOADS
        elif scan_type == "2":
            return "sql", SQLI_PAYLOADS
        else:
            print("❌ Invalid input. Please select either 1 or 2.")

class WebScanner:
    def __init__(self, url, scan_type, payloads):
        self.url = url
        self.scan_type = scan_type
        self.payloads = payloads
        self.results = []
        self.session = requests.Session()

    def run_scan(self, urls):
        """ Start scanning for vulnerabilities """
        if not self.url:
            print("❌ Invalid URL. Exiting scan.")
            return

        print(f"[+] Starting scan for {self.scan_type.upper()} vulnerabilities at {self.url}")

        for url in urls:
            self.scan_url(url)

        print("[+] Scan complete!")
        self.save_report()
        self.continue_scan()

    def scan_url(self, url):
        """ Scan a URL for vulnerabilities, handling exceptions properly """
        try:
            for payload in self.payloads:
                response = self.session.get(url, params={"q": payload}, verify=certifi.where(), timeout=5)
                if self.is_vulnerable(response, payload):
                    self.results.append(f"[!] Vulnerability detected in URL: {url} with payload: {payload}")
                    print(f"[+] Found vulnerability in URL: {url} with payload: {payload}")

            response = self.session.get(url, verify=certifi.where(), timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            forms = soup.find_all("form")

            for form in forms:
                form_action = form.get("action")
                form_method = form.get("method", "get").lower()
                inputs = form.find_all("input")

                for payload in self.payloads:
                    form_data = {input_field.get("name"): payload for input_field in inputs if input_field.get("name")}

                    if form_method == "post":
                        response = self.session.post(urljoin(url, form_action), data=form_data, verify=certifi.where(), timeout=5)
                    else:
                        response = self.session.get(urljoin(url, form_action), params=form_data, verify=certifi.where(), timeout=5)

                    if self.is_vulnerable(response, payload):
                        self.results.append(f"[!] Vulnerability detected in form submission at {url} with payload: {payload}")
                        print(f"[+] Found vulnerability in form at {url} with payload: {payload}")
        except requests.exceptions.MissingSchema:
            print(f"❌ Error: Invalid URL schema (Did you forget 'http://' or 'https://')? URL: {url}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Error: Failed to connect to {url}. Check if the website is live.")
        except requests.exceptions.Timeout:
            print(f"❌ Error: Connection timed out for {url}.")
        except requests.exceptions.HTTPError as err:
            print(f"❌ HTTP Error: {err}")
        except Exception as e:
            print(f"❌ Unexpected error while scanning {url}: {e}")

    def is_vulnerable(self, response, payload):
        """ Check if the response contains signs of vulnerability """
        return 'error' in response.text.lower() or payload in response.text

    def save_report(self):
        """ Save scan results to a JSON report """
        with open("scan_report.json", "w") as json_file:
            json.dump({"vulnerabilities": self.results}, json_file, indent=4)
        print("[+] Report saved as scan_report.json")

    def continue_scan(self):
        """ Offer options to continue scanning """
        choice = input("\nWould you like to:\n1. Scan for another vulnerability (XSS/SQL Injection)\n2. Test another site\n3. Stop the scan\nChoose 1, 2, or 3: ")

        if choice == "1":
            scan_type, payloads = get_scan_type()
            self.run_scan([self.url])
        elif choice == "2":
            self.start_scan()
        elif choice == "3":
            print("[+] Exiting the scan. Goodbye!")
            exit()
        else:
            print("[+] Invalid input. Exiting the scan.")
            exit()

    def start_scan(self):
        """ Start a new scan session """
        print("\nWelcome to the Web Vulnerability Scanner!")
        while True:
            user_url = get_valid_url()
            scan_type, payloads = get_scan_type()

            self.run_scan([user_url])
