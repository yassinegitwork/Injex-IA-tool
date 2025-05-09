 INJEX-IA: Web Vulnerability Scanner Tool



![screen7](https://github.com/user-attachments/assets/0c036f2e-9961-42e3-8f73-38ec28eb69af)




 

## Tool Description

**INJEX-IA** is a powerful, automated web vulnerability scanner designed for security researchers and developers. It helps to identify common vulnerabilities such as Cross-Site Scripting (XSS), SQL Injection (SQLi), and sensitive file exposure in web applications. 

The tool is modular, offering components for:
- **Web Crawling**: Automatically navigates websites, extracts links, forms, and input fields.
- **Payload Injection**: Injects predefined payloads to identify vulnerabilities like XSS, SQLi, and sensitive file exposure.
- **Vulnerability Detection**: Analyzes HTTP responses and identifies vulnerabilities, marking them with severity levels using AI models.
- **AI-Based Scanning**: The tool integrates an AI model that continuously learns from scan data to improve detection accuracy over time.
- **Reporting**: Generates detailed reports in JSON format, including vulnerability types and risk levels.

INJEX-IA is a comprehensive tool for automating vulnerability scanning, detecting weaknesses in web applications, and assisting in improving security measures.

---

## How to Run INJEX-IA

Follow these simple steps to launch INJEX-IA on your Kali Linux machine.

1. **Clone the Repository**

Start by cloning the repository from GitHub to your local machine:

--git clone https://github.com/yassinegitwork/Injex-IA-tool.git
--cd INJEX-IA

2. Install Dependencies
INJEX-IA uses several Python libraries to function. Install them using pip:
pip install -r requirements.txt
This will install all the required dependencies to run the tool.

3. Install Web Browser Drivers
For browser automation, INJEX-IA requires ChromeDriver (for Chrome) and GeckoDriver (for Firefox). Make sure you install the correct version of each driver based on the browser version you are using.

3.1 Installing ChromeDriver
To install ChromeDriver on Kali Linux:
sudo apt-get update
sudo apt-get install chromium-chromedriver
Important Note:
Check your Chrome version before installing ChromeDriver to ensure compatibility.

To check your Chrome version, run:
chromium --version
Download the appropriate ChromeDriver version from ChromeDriver's official page.

After installation, ensure the chromedriver is accessible in your terminal:
which chromedriver
If it's not in the correct path, add the driver to your PATH environment variable:
nano ~/.bashrc
Add the following line at the end of the file:

export PATH=$PATH:/usr/lib/chromium-browser/chromedriver
After saving the file, run:
source ~/.bashrc
3.2 Installing GeckoDriver (Firefox)
To install GeckoDriver for Firefox:
sudo apt-get install firefox-geckodriver

Important Note:
Check your Firefox version before installing GeckoDriver to ensure compatibility.

To check your Firefox version, run:
firefox --version
Download the correct version of GeckoDriver from GeckoDriver's official page.

After installation, make sure the geckodriver is in your system path:


which geckodriver
-Check Results in scan_report.json and Metrics in metrics.json
-Once your scan has completed, INJEX-IA will generate two important files containing the results:

1. Scan Results: scan_report.json
-scan_report.json contains all the findings from the scan, including both true positives and false positives. It lists all identified vulnerabilities, their severity levels, affected URLs, and payloads used.

You can view the results by opening the file in any text editor or by using the following command in the terminal:

cat scan_report.json


2. Metrics: metrics.json
metrics.json contains key performance metrics of the scan. This file helps track the effectiveness of your scanning process and includes important data for retraining the AI model to improve detection accuracy.

You can check the metrics with:

cat metrics.json
-Both files will help you understand the scan results and assist in refining the security posture of the tested web applications.

-Additional Notes
Version Compatibility: Always ensure you download the correct version of ChromeDriver or GeckoDriver to match the versions of Chrome or Firefox you have installed.

Chrome/Firefox Path Configuration: If necessary, you can adjust the browser driver path manually within the code or set the PATH environment variable to point to the location of your downloaded drivers.
