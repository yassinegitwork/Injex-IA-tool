from scanner.scanner import WebScanner
from scanner.crawler import WebCrawler
from scanner.payloads import XSS_PAYLOADS, SQLI_PAYLOADS, SENSITIVE_FILES
import pyfiglet
import re
from urllib.parse import urlparse
from train_model import train_model

def print_banner():
    tool_name_ascii = pyfiglet.figlet_format("INJEX-IA")
    banner = f"""
    ================================================
    =          🕷️ Injex-IA: Web Vulnerability Scanner 🔎       =
    =            POWERED BY YASSINE SOUSSI            =
    ================================================

    {tool_name_ascii}

    🕷️  Scanning the web for vulnerabilities... Stay secure!  🔎
    ============================================================== 
    """
    print("\033[1;32m" + banner + "\033[0m")

def format_url(url):
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        return "http://" + url  # Default to HTTP (not HTTPS)
    return url

def is_valid_url(url):
    pattern = re.compile(
        r"^(https?://)"                       # http or https
        r"(localhost|"                        # localhost
        r"127\.0\.0\.1|"                      # loopback IP
        r"\d{1,3}(\.\d{1,3}){3}|"             # other IP addresses
        r"([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}))"    # or domain
        r"(:\d{1,5})?"                        # optional port
        r"(/.*)?$"                            # optional path
    )
    match = pattern.match(url)
    if match:
        domain = match.group(2)
        if domain and ('...' in domain or '..' in domain):
            return False
        return True
    return False

def get_valid_url():
    while True:
        url = input("[+] Please enter the target URL: ").strip()
        formatted_url = format_url(url)
        if is_valid_url(formatted_url):
            return formatted_url
        print("❌ Invalid URL format. Please enter a valid URL (e.g., http://localhost:8080, http://127.0.0.1, or https://example.com)")

def choose_scan_type():
    while True:
        print("[+] Choose the scan type:")
        print("[1] XSS Scan")
        print("[2] SQL Injection Scan")
        print("[3] Sensitive Files & Directory Listing Scan")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "xss", XSS_PAYLOADS
        elif choice == "2":
            return "sql", SQLI_PAYLOADS
        elif choice == "3":
            return "sensitive", SENSITIVE_FILES
        print("❌ Invalid input. Please select 1, 2, or 3.")

def choose_next_action():
    while True:
        print("[1] Scan for another vulnerability")
        print("[2] Test another site")
        print("[3] Exit")
        choice = input("Choose 1, 2, or 3: ")
        if choice in ["1", "2", "3"]:
            return choice
        print("❌ Invalid choice, please select 1, 2, or 3.")

def main():
    print_banner()
    url = get_valid_url()
    scan_type, payloads = choose_scan_type()

    crawler = WebCrawler(url)
    discovered_urls = crawler.crawl()

    scanner = WebScanner(url, scan_type, payloads)
    scanner.run_scan(discovered_urls)

    while True:
        next_action = choose_next_action()
        if next_action == "1":
            scan_type, payloads = choose_scan_type()
            scanner.scan_type = scan_type
            scanner.payloads = payloads
            scanner.run_scan(discovered_urls)
        elif next_action == "2":
            main()
            return
        elif next_action == "3":
            print("[+] Exiting...")
            break

    print("[*] Auto-training the model with the latest scan data...")
    train_model()  # Trigger model retraining after all scans

if __name__ == "__main__":
    main()
