# main.py
from scanner.scanner import WebScanner
from scanner.crawler import WebCrawler
from scanner.payloads import XSS_PAYLOADS, SQLI_PAYLOADS, SENSITIVE_FILES
import pyfiglet
import re
from urllib.parse import urlparse

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
        return "https://" + url  # Enforcing HTTPS scheme
    return url

def is_valid_url(url):
    pattern = re.compile(r"^https://([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,})?(:\d{1,5})?(/.*)?$")
    match = pattern.match(url)
    if match:
        domain = match.group(1)
        if '...' in domain or '..' in domain:
            return False
        return True
    return False

def get_valid_url():
    while True:
        url = input("[+] Please enter the target URL: ").strip()
        formatted_url = format_url(url)
        if is_valid_url(formatted_url):
            return formatted_url
        print("❌ Invalid URL format. Please enter a valid URL (e.g., https://example.com)")

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

if __name__ == "__main__":
    main()
