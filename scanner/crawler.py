import os
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.visited = set()
        self.discovered = set()
        self.driver = self._init_driver()

    def _init_driver(self):
        print("[*] Initializing browser driver...")

        driver_paths = {
            "chrome": os.path.join("drivers", "chromedriver.exe"),
            "firefox": os.path.join("drivers", "geckodriver.exe"),
            "edge": os.path.join("drivers", "msedgedriver.exe"),
        }

        # Try Chrome
        try:
            options = ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Set the binary location for Chrome
            service = ChromeService(executable_path=driver_paths["chrome"])
            driver = webdriver.Chrome(service=service, options=options)
            print("[+] Using Selenium Chrome driver.")
            return driver
        except Exception as e:
            print(f"[!] Chrome driver failed: {e}")

        # Try Firefox
        try:
            options = FirefoxOptions()
            options.add_argument("--headless")
            service = FirefoxService(executable_path=driver_paths["firefox"])
            driver = webdriver.Firefox(service=service, options=options)
            print("[+] Using Selenium Firefox driver.")
            return driver
        except Exception as e:
            print(f"[!] Firefox driver failed: {e}")

        print("[!] All Selenium drivers failed. Falling back to requests + BeautifulSoup mode.")
        return None

    def make_request(self, url, retries=3, timeout=5):
        attempt = 0
        while attempt < retries:
            try:
                print(f"[*] Attempting to request: {url} (Attempt {attempt + 1} of {retries})")
                response = requests.get(url, timeout=timeout)
                response.raise_for_status()
                return response
            except requests.exceptions.Timeout:
                print(f"[!] Timeout occurred for {url}. Retrying...")
            except requests.exceptions.RequestException as e:
                print(f"[!] Request failed for {url}: {e}")
            attempt += 1
            time.sleep(2)
        return None

    def crawl(self, max_depth=2):
        print(f"[+] Starting to crawl {self.base_url}")
        self._crawl_url(self.base_url, 0, max_depth)
        print(f"[+] Discovered {len(self.discovered)} pages.")
        return list(self.discovered)

    def _crawl_url(self, url, depth, max_depth):
        if depth > max_depth or url in self.visited:
            return

        self.visited.add(url)

        try:
            if self.driver:
                self.driver.get(url)
                time.sleep(1)
                page_source = self.driver.page_source
            else:
                response = self.make_request(url)
                if response and response.status_code == 200:
                    page_source = response.text
                else:
                    print(f"[!] Failed to fetch {url}, skipping.")
                    return

            self.discovered.add(url)
            soup = BeautifulSoup(page_source, "html.parser")
            for link in soup.find_all("a", href=True):
                href = link['href']
                next_url = urljoin(url, href)
                if self._is_valid_url(next_url):
                    self._crawl_url(next_url, depth + 1, max_depth)

        except Exception as e:
            print(f"[!] Error crawling {url}: {e}")

    def _is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.netloc == urlparse(self.base_url).netloc and url not in self.visited

    def close(self):
        if self.driver:
            self.driver.quit()
