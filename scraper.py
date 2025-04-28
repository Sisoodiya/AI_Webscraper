# Description: This file contains the code to scrape a website using
# selenium and local chromedriver.

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Selenium allows us to control the browser using code it allows us to perform activities like click buttons, Interact with text widgets etc.
# We can use it to scrape websites that require javascript to render the page.
# bs4 is a Python library used for web scraping. It allows you to parse HTML and XML documents, extract data, and manipulate the content.
# BeautifulSoup is a class in the bs4 library that provides methods for parsing and navigating HTML documents.

def scrape_website(website :str) :
    """
    Scrapes a website using Selenium WebDriver and returns its HTML content.
    :param website: The URL of the website to scrape
    :return: The HTML source of the webpage as a string
    """

    print(f"Launching local chrome browser for {website}...")

    # We need to specify where our chrome driver is
    # This is the path to the chrome driver - update this path if needed
    chrome_driver_path : str = "./chromedriver" 

    # Create Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Uncomment the line below to run Chrome in headless mode (without GUI)
    # options.add_argument("--headless")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website) # Navigate to the website
        print("Page loaded! Scraping page content...")
        
        # Wait for the page to load completely
        time.sleep(5)
        
        # Get the page source
        html = driver.page_source
        return html
    finally:
        driver.quit() # Make sure to close the browser

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
    return ""

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

"""
Note on Web Scraping:
When scraping websites like 'amazon.com', you may encounter CAPTCHA pages.
This is because these websites implement anti-bot measures to prevent automated scraping.
Excessive scraping attempts may result in your IP being blocked.

Possible solutions:
1. Use a headless browser (uncomment the headless option above)
2. Add random delays between requests
3. Rotate user agents
4. Use proxy services like Brightdata (implemented in scrape.py)

Toggle between local scraping and Brightdata by changing the import in main.py:
- For local Chrome: from scraper import *
- For Brightdata: from scrape import *
"""