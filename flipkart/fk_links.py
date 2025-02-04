import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.flipkart.com/headset/pr?sid=fcn&otracker=categorytree&page="
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

def get_product_links(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Failed to retrieve page {url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    product_links = []
    
    links = soup.find_all("a", attrs={"class": "DMMoT0"})  # Flipkart product link class
    for link in links: 
        href = link.get("href")
        if href:
            product_links.append("https://www.flipkart.com" + href)
    
    return product_links

# # Collect links from multiple pages
# all_links = []
# for i in range(1, 20):  # Pages 1 to 5
#     page_links = get_product_links(URL + str(i))
#     all_links.extend(page_links)

i=0
all_links=[]
while len(all_links) <1000:
    page_links = get_product_links(URL + str(i))
    all_links.extend(page_links)
    i=i+1

# Save to CSV
df = pd.DataFrame(all_links, columns=["Product Link"])
df.to_csv("fk_headphones.csv", index=False)

print("Scraping completed. Data saved to fk_headphones.csv")
