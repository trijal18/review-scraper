from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

data = []

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15")

# Function to get product links
def get_links(driver):
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    product_divs = driver.find_elements(By.CSS_SELECTOR, "div.a-column.a-span12.a-text-center._cDEzb_grid-column_2hIsc")
    for div in product_divs:
        try:
            link = div.find_element(By.TAG_NAME, "a").get_attribute("href")
            if link:
                data.append(link)
        except Exception as e:
            print(f"Error fetching link: {e}")

def main():
    # Set up Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        # First page
        url1 = "https://www.amazon.in/gp/bestsellers/electronics/5605728031/ref=zg_bs_pg_1_electronics?ie=UTF8&pg=1"
        driver.get(url1)
        time.sleep(5)  # Give time for the page to load
        get_links(driver)
        
        # Second page
        url2 = "https://www.amazon.in/gp/bestsellers/electronics/5605728031/ref=zg_bs_pg_2_electronics?ie=UTF8&pg=2"
        driver.get(url2)
        time.sleep(5)
        get_links(driver)
        
        # Save to CSV
        df = pd.DataFrame(data, columns=["Product Link"])
        df.to_csv("amz_links_selenium.csv", index=False)
        print(f"Scraped {len(data)} links and saved to amz_links_selenium.csv")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
