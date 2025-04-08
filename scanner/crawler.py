import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()
        self.discovered_urls = set()
        logging.basicConfig(filename="crawler_log.txt", level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")

    def crawl(self):
        self._crawl_page(self.base_url)
        print(f"[+] Discovered {len(self.discovered_urls)} pages.")
        return list(self.discovered_urls)

    def _crawl_page(self, url):
        if url in self.visited:
            return
        self.visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if self._is_same_domain(full_url):
                    self.discovered_urls.add(full_url)
                    self._crawl_page(full_url)
        except Exception as e:
            logging.error(f"Failed to crawl {url} - {e}")

    def _is_same_domain(self, url):
        return urlparse(url).netloc == urlparse(self.base_url).netloc