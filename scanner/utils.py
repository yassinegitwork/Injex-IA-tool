import json
import logging
from bs4 import BeautifulSoup

# Function to extract forms from the HTML content of a page
def extract_forms(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all("form")

# Function to save the scan report in different formats (txt, json, html)
def save_report(results, report_type):
    if report_type == "json":
        with open("scan_report.json", "w") as json_file:
            json.dump({"vulnerabilities": results}, json_file, indent=4)
        print("[+] Report saved as scan_report.json")

    elif report_type == "txt":
        with open("scan_report.txt", "w") as txt_file:
            for result in results:
                txt_file.write(result + "\n")
        print("[+] Report saved as scan_report.txt")
    
    elif report_type == "html":
        with open("scan_report.html", "w") as html_file:
            html_file.write("<html><body><h1>Scan Report</h1><ul>")
            for result in results:
                html_file.write(f"<li>{result}</li>")
            html_file.write("</ul></body></html>")
        print("[+] Report saved as scan_report.html")

# Function to set up logging
def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
