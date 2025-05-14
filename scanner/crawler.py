from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio

class WebCrawler:
    def __init__(self, base_url, browser_type="chromium"):
        self.base_url = base_url.rstrip('/')
        self.visited = set()
        self.discovered = set()
        self.browser_type = browser_type

    async def fetch_page(self, page, url):
        try:
            await page.route("**/*", lambda route, request: route.abort() 
                             if request.resource_type in ["image", "stylesheet", "font"] 
                             else route.continue_())
            await page.goto(url, timeout=30000, wait_until="domcontentloaded")
            await page.wait_for_timeout(2000)
            return await page.content()
        except Exception:
            return None

    async def _crawl_url(self, browser, url, depth, max_depth):
        if depth > max_depth or url in self.visited:
            return
        self.visited.add(url)
        page = await browser.new_page()
        try:
            page_source = await self.fetch_page(page, url)
            if not page_source:
                return
            self.discovered.add(url)
            soup = BeautifulSoup(page_source, "html.parser")
            tasks = []
            for link in soup.find_all("a", href=True):
                href = link['href']
                next_url = urljoin(url, href)
                if self._is_valid_url(next_url):
                    tasks.append(self._crawl_url(browser, next_url, depth + 1, max_depth))
            await asyncio.gather(*tasks)
        finally:
            await page.close()

    def _is_valid_url(self, url):
        parsed = urlparse(url)
        return parsed.netloc == urlparse(self.base_url).netloc and url not in self.visited

    async def crawl(self, max_depth=3):
        print(f"[+] Starting crawl with Playwright: {self.base_url}")
        async with async_playwright() as p:
            browser = await {
                "firefox": p.firefox,
                "webkit": p.webkit,
                "chromium": p.chromium
            }.get(self.browser_type, p.chromium).launch(headless=True)

            try:
                await self._crawl_url(browser, self.base_url, 0, max_depth)
            finally:
                await browser.close()

        print(f"[+] Discovered {len(self.discovered)} pages.")
        return list(self.discovered)
