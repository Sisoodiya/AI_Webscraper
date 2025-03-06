import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website :str):
    print(f"Launching chrome browser for {website}...")

    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = Service(chrome_driver_path), options = options)

    try :
        driver.get(website)
        print(f"Page Loaded...")
        html = driver.page_source

        return html
    finally :
        driver.quit()