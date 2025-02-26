from scanner.scanner import WebScanner
from scanner.crawler import WebCrawler
from scanner.payloads import XSS_PAYLOADS, SQLI_PAYLOADS
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
        return "https://" + url
    return url

def is_valid_url(url):
    """ Validate the URL format (http or https) and ensure it's a valid domain """
    pattern = re.compile(r"^(https?://)?([a-zA-Z0-9.-]+)(\.[a-zA-Z]{2,})?(:\d{1,5})?(/.*)?$")
    match = pattern.match(url)
    
    # Ensure the domain part is at least 2 characters long and is valid
    if match:
        domain = match.group(2)  # The domain part (without the protocol)
        # Reject domain names with invalid characters like '...'
        if '...' in domain or '..' in domain:
            return False
        return True
    return False


def get_valid_url():
    while True:
        url = input("[+] Please enter the target URL: ").strip()
        formatted_url = format_url(url)  # Ensure URL has 'http://' or 'https://'
        if is_valid_url(formatted_url):
            return formatted_url
        else:
            print("❌ Invalid URL format. Please enter a valid URL (e.g., https://example.com)")


def choose_scan_type():
    """Prompt the user to choose a scan type and handle invalid inputs."""
    while True:
        try:
            print("[+] Choose the scan type:")
            print("[1] XSS Scan")
            print("[2] SQL Injection Scan")
            scan_type = input("Enter 1 or 2: ").strip()
            if scan_type == "1":
                return "xss", XSS_PAYLOADS
            elif scan_type == "2":
                return "sql", SQLI_PAYLOADS
            else:
                raise ValueError("❌ Invalid input. Please select either 1 or 2.")
        except ValueError as e:
            print(e)
            continue  # Prompt the user again if the input is invalid

def choose_next_action():
    """Prompt the user to choose the next action and handle invalid inputs."""
    while True:
        print("[1] Scan for another vulnerability (XSS/SQL Injection)")
        print("[2] Test another site")
        print("[3] Stop the scan")
        choice = input("Choose 1, 2, or 3: ")

        if choice == "1":
            return "scan_another"   
        elif choice == "2":
            return "test_another_site"
        elif choice == "3":
            print("[+] Stopping the scan.")
            return "stop_scan"
        else:
            # No need to raise an exception here; just print the error and re-ask.
            print("❌ Invalid input. Please choose 1, 2, or 3.")
            continue  # Reask the user for a valid choice

def main():
    print_banner()

    # First ask for URL input and validate it
    url = get_valid_url()
    print(f"[+] Valid URL: {url}")
    
    # Now ask for scan type after URL validation
    scan_type, payloads = choose_scan_type()
    if scan_type:
        print(f"[+] Starting {scan_type} on {url}")
        
        # Crawl the discovered URLs from the provided base URL
        crawler = WebCrawler(url)
        discovered_urls = crawler.crawl()

        print("[+] Discovered URLs:")
        for u in discovered_urls:
            print(u)

        # Start scanning the discovered URLs
        scanner = WebScanner(url, scan_type, payloads)
        scanner.run_scan(discovered_urls)

        # Ask the user what to do next after the scan completes
        next_action = choose_next_action()

        if next_action == "scan_another":
            main()  # Restart the process for scanning another vulnerability
        elif next_action == "test_another_site":
            main()  # Restart the process for testing another site
        else:
            print("[+] Scan stopped.")
    else:
        print("[+] Scan stopped.")


if __name__ == "__main__":
    main()
