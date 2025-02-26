import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.session = requests.Session()

    def crawl(self):
        print("[+] Starting to crawl the site...")
        to_crawl = [self.base_url]
        discovered_urls = set()

        while to_crawl:
            current_url = to_crawl.pop(0)
            if current_url not in self.visited_urls:
                self.visited_urls.add(current_url)
                try:
                    response = self.session.get(current_url)
                    soup = BeautifulSoup(response.text, "html.parser")

                    # Find all links on the page and add internal ones to the crawl list
                    for link in soup.find_all("a", href=True):
                        href = link.get("href")
                        full_url = urljoin(current_url, href)
                        
                        # If the link is internal, add it to the to_crawl list
                        if self.is_internal_url(full_url):
                            if full_url not in self.visited_urls:
                                to_crawl.append(full_url)
                                discovered_urls.add(full_url)

                except requests.RequestException as e:
                    print(f"[Error] Failed to access {current_url}: {e}")

        return list(discovered_urls)

    def is_internal_url(self, url):
        # Ensure the URL is internal to the same domain
        return urlparse(url).netloc == urlparse(self.base_url).netloc

    def is_valid_url(self, url):
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

    def format_url(self, url):
        """ Ensure the URL starts with http:// or https://, default to https """
        if not url.startswith(("http://", "https://")):
            print("⚠️ No protocol specified. Defaulting to HTTPS...")
            return "https://" + url
        return url
