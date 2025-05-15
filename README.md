
# INJEX-IA: Web Vulnerability Scanner Tool

![screen7](https://github.com/user-attachments/assets/7d4928b5-0db3-4033-87b2-e1d5fe188f01)

---

## 🔍 Tool Description

**INJEX-IA** is a powerful, automated web vulnerability scanner designed for security researchers and developers. It helps identify common vulnerabilities such as:

- **Cross-Site Scripting (XSS)**
- **SQL Injection (SQLi)**
- **Sensitive File Exposure**

### The tool includes the following core modules:

- **Web Crawling**: Automatically navigates websites, extracts links, forms, and input fields.
- **Payload Injection**: Injects predefined payloads to test for XSS, SQLi, and sensitive file exposures.
- **Vulnerability Detection**: Analyzes HTTP responses and flags vulnerabilities with severity levels using AI models.
- **AI-Based Scanning**: Continuously improves detection accuracy by learning from scan results.
- **Reporting**: Generates comprehensive reports in JSON format, including vulnerability types, affected URLs, payloads, and risk levels.

---

## ⚙️ Installation Guide for Kali Linux (Selenium-Based)

Follow these steps to install and run **INJEX-IA** using **Selenium** with automatic browser driver management:

### 1. Clone the Repository
```bash
git clone https://github.com/yassinegitwork/Injex-IA-tool.git
cd Injex-IA-tool
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```
This installs all the necessary Python libraries including selenium.

### 3. Install webdriver-manager for Automatic Driver Management
```bash
pip install webdriver-manager
```

🌐 Automatic Web Browser Driver Management  
Thanks to webdriver-manager, INJEX-IA automatically downloads and manages the correct versions of browser drivers (ChromeDriver, GeckoDriver, EdgeDriver) matching your installed browsers.

Drivers are typically saved in system paths like /usr/local/bin or managed internally by the package.

You do NOT need to manually download or install any drivers anymore!

🔧 Browser Executable Paths on Kali Linux  
Make sure Selenium can find your installed browsers by specifying their paths in the code. Typical paths for Kali Linux are:

- Google Chrome: /usr/bin/google-chrome
- Mozilla Firefox: /usr/bin/firefox
- Microsoft Edge: /usr/bin/microsoft-edge

You can verify these paths by running:

```bash
which google-chrome
which firefox
which microsoft-edge
```

🛠️ Verify Browser Driver Paths  
If you want to verify where your browser drivers are installed, try running:

```bash
which chromedriver
which geckodriver
which msedgedriver
```

These commands should output paths like /usr/local/bin/chromedriver if the drivers are installed and accessible in your system PATH.

🌐 Manual Web Browser Driver Management  
**Updating system and installing required tools**
sudo apt update
sudo apt install -y wget curl unzip tar

# ChromeDriver (latest stable)
CHROME_VER=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+')
wget -N https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VER -O chrome_ver.txt
CHROME_DRIVER_VER=$(cat chrome_ver.txt)
wget -N https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VER/chromedriver_linux64.zip
unzip -o chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver

# GeckoDriver (Firefox)
GECKO_VER=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
wget https://github.com/mozilla/geckodriver/releases/download/v$GECKO_VER/geckodriver-v$GECKO_VER-linux64.tar.gz
tar -xzf geckodriver-v$GECKO_VER-linux64.tar.gz
sudo mv geckodriver /usr/local/bin/geckodriver
sudo chmod +x /usr/local/bin/geckodriver

# EdgeDriver
EDGE_VER=$(curl -s https://msedgedriver.azureedge.net/LATEST_STABLE)
wget https://msedgedriver.azureedge.net/$EDGE_VER/edgedriver_linux64.zip
unzip -o edgedriver_linux64.zip
sudo mv msedgedriver /usr/local/bin/msedgedriver
sudo chmod +x /usr/local/bin/msedgedriver


🚀 Running INJEX-IA  
Once setup is complete, start the tool with:

```bash
python main.py
```

You will be prompted to enter:

- The target URL
- The type of scan: XSS, SQL Injection, or Sensitive Files
- The browser to use: chrome, firefox, or edge

Example:

```bash
python main.py --url https://target.com --browser chrome
```

📁 Scan Results  
After a scan completes, the tool will generate two important files:

1. scan_report.json  
Contains:

- All detected vulnerabilities (true positives and false positives)
- Vulnerability types and severity
- Affected URLs and payloads used

To view:

```bash
cat scan_report.json
```

2. metrics.json  
Contains:

- Performance metrics of the scan
- Data useful for AI model improvement

To view:

```bash
cat metrics.json
```

📌 Notes  
✅ Selenium-based scanning with real browser control  
🔄 Supports Chrome, Firefox, and Edge browsers  
🔧 Drivers are automatically managed by webdriver-manager and typically saved in /usr/local/bin  
🛡️ Optimized for penetration testing and secure development workflows

Enjoy scanning securely with INJEX-IA — Powered by Yassine Soussi.
