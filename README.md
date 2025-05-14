INJEX-IA: Web Vulnerability Scanner Tool


![screen7](https://github.com/user-attachments/assets/7d4928b5-0db3-4033-87b2-e1d5fe188f01)




Tool Description
INJEX-IA is a powerful, automated web vulnerability scanner designed for security researchers and developers. It helps identify common vulnerabilities such as:

Cross-Site Scripting (XSS)

SQL Injection (SQLi)

Sensitive file exposure

The tool includes the following core modules:
Web Crawling: Automatically navigates websites, extracts links, forms, and input fields.

Payload Injection: Injects predefined payloads to test for XSS, SQLi, and sensitive file exposures.

Vulnerability Detection: Analyzes HTTP responses and flags vulnerabilities with severity levels using AI models.

AI-Based Scanning: Continuously improves detection accuracy by learning from scan results.

Reporting: Generates comprehensive reports in JSON format, including vulnerability types, affected URLs, payloads, and risk levels.

How to Run INJEX-IA on Kali Linux
Follow these steps to install and run INJEX-IA using Playwright:

1. Clone the Repository
git clone https://github.com/yassinegitwork/Injex-IA-tool.git
cd INJEX-IA

3. Install Python Dependencies
pip install -r requirements.txt
This installs all the necessary Python libraries including Playwright.

3. Install and Configure Playwright
INJEX-IA uses Playwright for browser automation, supporting Chromium, Firefox, and WebKit.

Install Playwright and its browser binaries by running:

pip install playwright
python -m playwright install
✅ This command will automatically download the required browsers, so no manual setup of ChromeDriver or GeckoDriver is needed.

4. (Optional) Enable Browser GUI for Debugging
By default, Playwright runs browsers in headless mode (no UI). To run with a visible browser window (for debugging or visual confirmation), edit the crawler code to set:

browser = await p.chromium.launch(headless=False)
Running INJEX-IA
Once setup is complete, run the tool:


python main.py
You will be prompted to enter:

The target URL

The type of scan: XSS, SQL Injection, or Sensitive Files

Scan Results
After a scan completes, the tool will generate two important files:

1. scan_report.json
Contains:

All detected vulnerabilities (true positives and false positives)

Vulnerability types and severity

Affected URLs and payloads used

To view:
cat scan_report.json

2. metrics.json
Contains:
Performance metrics of the scan
Data useful for AI model improvement

To view:
cat metrics.json

Notes
✅ No driver setup required — Playwright handles browsers internally.

🔁 Cross-browser support — Easily switch between Chromium, Firefox, or WebKit.

🛠️ Runs out of the box on Kali Linux without any special environment variables or manual configurations.

Enjoy scanning securely with INJEX-IA — Powered by Yassine Soussi.
