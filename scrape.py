# Description: This file contains the code to scrape a website using
# selenium and Brightdata.

from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Web scraping is the process of extracting data from websites. This data can be used for various purposes, such as data analysis, research, or automation.
# bs4 is a Python library used for web scraping. It allows you to parse HTML and XML documents, extract data, and manipulate the content.
# BeautifulSoup is a class in the bs4 library that provides methods for parsing and navigating HTML documents.
# An HTML parser is a software tool that analyzes HTML code to identify its structure and extract information.
# It breaks down the HTML into its component parts, such as tags, attributes, and text

AUTH = 'write_your_username_here:write_your_password_here'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website :str) :
    """
    Scrapes a website using Selenium WebDriver and returns its HTML content.
    :param website: The URL of the website to scrape
    :return: The HTML source of the webpage as a string
    """

    print(f"Launching chrome browser for {website}...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        # print('Taking page screenshot to file page.png')
        # driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body_content(html_content :str) -> str :
    """
    Extracts the body content from the HTML source.
    :param html_content: The HTML source of the webpage
    :return: The body content of the webpage as a string
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content :
        return str(body_content)
    return f""

def clean_body_content(body_content :str) -> str :
    """
    Cleans the body content by removing all script and style tags.
    :param body_content: The body content of the webpage
    :return: The cleaned body content as a string
    """
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract() # Will remove the script and style tags.

    # Get the text content of the webpage and remove any leading or trailing whitespace.
    cleaned_content = soup.get_text(separator = "\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    ) # Remove any empty lines.
    return cleaned_content

def split_dom_content(dom_content : str, max_length : int = 6000) -> list :
    """
    Splits the DOM content into chunks of a maximum length.
    :param dom_content: The DOM content of the webpage
    :param max_length: The maximum length of each chunk
    :return: A list of chunks of the DOM content
    """
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
