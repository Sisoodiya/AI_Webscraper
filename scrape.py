# Description: This file contains the code to scrape a website using
# selenium and chromedriver.
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service


# Selenium allows us to control the browser using code it allows us to perform activities like click buttons, Interact with text widgets etc.
# We can use it to scrape websites that require javascript to render the page.
def scrape_website(website :str) :
    """
    Scrapes a website using Selenium WebDriver and returns its HTML content.
    :param website: The URL of the website to scrape
    :return: The HTML source of the webpage as a string
    """

    print(f"Launching chrome browser for {website}...")

    # We need to specify where our chrome drivers is
    # This is actually an Application that we will need to download.
    # That will allow us to control chrome.
    # We can download it from https://sites.google.com/a/chromium.org/chromedriver/downloads
    chrome_driver_path : str = ""


    options = webdriver.ChromeOptions() # We options so we can specify how the web driver should operate.
    driver = webdriver.Chrome(service = Service(chrome_driver_path), options = options)
    # We Set up our actual drivers in the above line with the options and services we want to access that will be wherever the chrome driver lives.

    try :
        driver.get(website) #
        print(f"Page Loaded...")
        html = driver.page_source
        return html
    finally :
        driver.quit()