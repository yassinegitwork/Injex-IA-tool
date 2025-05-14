##INJEX-IA: Web Vulnerability Scanner Tool


**INJEX-IA** is a powerful, automated web vulnerability scanner designed for security researchers and developers. It helps identify common vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (SQLi), and sensitive file exposure in web applications.
=======


![screen7](https://github.com/user-attachments/assets/0c036f2e-9961-42e3-8f73-38ec28eb69af)




 

**Tool Description**

**The tool is modular, offering components for:**

**-Web Crawling:** Automatically navigates websites, extracts links, forms, and input fields.

**-Payload Injection:** Injects predefined payloads to test for XSS, SQLi, and sensitive file exposures.

**-Vulnerability Detection:** Analyzes HTTP responses and flags vulnerabilities with severity levels using AI models.

**-AI-Based Scanning:** The AI model improves detection accuracy by learning from scan data over time.

**-Reporting:** Generates comprehensive reports in JSON format, including vulnerability details and risk levels.

INJEX-IA is a comprehensive tool for automating vulnerability scanning, detecting weaknesses in web applications, and assisting in improving security measures.



**How to Run INJEX-IA on Kali Linux** 
**Follow these steps to install and run INJEX-IA using Playwright:**

**1. Clone the Repository**
git clone https://github.com/your-repo/INJEX-IA.git
cd INJEX-IA

**2. Install Python Dependencies**
=======
1. **Clone the Repository**

Start by cloning the repository from GitHub to your local machine:

**git clone https://github.com/yassinegitwork/Injex-IA-tool.git**

**cd INJEX-IA**

2. **Install Dependencies**
**INJEX-IA uses several Python libraries to function. Install them using pip:**
pip install -r requirements.txt
This installs all the necessary libraries including Playwright.


**3. Install and Configure Playwright**
INJEX-IA uses Playwright for browser automation. Playwright supports Chromium, Firefox, and WebKit.

**Run the following to install Playwright and its browser engines:**
pip install playwright
python -m playwright install
✅ This will automatically download Chromium, Firefox, and WebKit browsers.

3. **Install Web Browser Drivers**
For browser automation, INJEX-IA requires ChromeDriver (for Chrome) and GeckoDriver (for Firefox). Make sure you install the correct version of each driver based on the browser version you are using.

3.1 **Installing ChromeDriver**
To install ChromeDriver on Kali Linux:
sudo apt-get update
sudo apt-get install chromium-chromedriver
Important Note:
Check your Chrome version before installing ChromeDriver to ensure compatibility.

**4. (Optional) Running Browsers in Non-Headless Mode**
Playwright runs browsers in headless mode (no UI) by default. To see the browser window while crawling or testing, you can edit the code like this:
python

browser = await p.chromium.launch(headless=False)
This can help with debugging or visual verification during scans.

Running INJEX-IA
**After setup, start the tool by running:**
python main.py

**You will be prompted to enter:**
The target URL
The type of scan: XSS, SQL Injection, or Sensitive Files
Understanding Scan Results

**After a scan completes, two files will be generated:**
**1. scan_report.json**
**This file contains:**
All findings (true positives and false positives)
Vulnerability types
Risk levels
Affected URLs
Payloads used

View it using:
cat scan_report.json

**2. metrics.json**
This file contains scan performance metrics that help:
Monitor scanning effectiveness
Support future AI model retraining
**View it using:**
cat metrics.json


**Notes**
Playwright Binaries: No need to manually install ChromeDriver or GeckoDriver. Playwright manages and runs the browsers internally.

Cross-Browser Support: You can easily switch between Chromium, Firefox, or WebKit by changing a single line in the crawler configuration.

Environment Variables: No extra environment configuration is required for Playwright. It works out of the box on Kali Linux.

Enjoy scanning securely with INJEX-IA — Powered by Yassine Soussi.
