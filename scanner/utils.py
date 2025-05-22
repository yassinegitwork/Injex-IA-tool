import json
import logging
from bs4 import BeautifulSoup

# Function to extract forms from the HTML content of a page
def extract_forms(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("form")

# Function to save the scan report in different formats (txt, json, html)
def save_report(results):
    with open("scan_report.json", "w") as json_file:
        json.dump({"vulnerabilities": results}, json_file, indent=4)
    print("[+] Report saved as scan_report.json")


# Function to set up logging
def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
