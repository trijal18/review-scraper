import requests
from bs4 import BeautifulSoup
import pandas as pd
data=[]
custom_headers = {
    "Accept-language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
}

def get_soup(url):
    response = requests.get(url, headers=custom_headers)

    if response.status_code != 200:
        print("Error in getting webpage")
        exit(-1)

    soup = BeautifulSoup(response.text, "lxml")
    return soup

def get_links(soup):
    links = soup.find_all("div", {"class": "a-column a-span12 a-text-center _cDEzb_grid-column_2hIsc"})
    for link in links:
        # link=link.find_all('a', href=True)
        # print(link.a["href"])
        data.append("https://www.amazon.in/"+link.a["href"])

def main():
    # search_url = "https://www.amazon.in/gp/bestsellers/electronics/1389365031/ref=zg_bs_pg_1_electronics?ie=UTF8&pg=1"
    soup = get_soup("https://www.amazon.in/gp/bestsellers/electronics/5605728031/ref=zg_bs_pg_2_electronics?ie=UTF8&pg=1")
    get_links(soup)
    soup = get_soup("https://www.amazon.in/gp/bestsellers/electronics/5605728031/ref=zg_bs_pg_2_electronics?ie=UTF8&pg=2")
    get_links(soup)
    df = pd.DataFrame(data=data)
    df.to_csv("amz_links_3.csv")
    print(data)

if __name__ == '__main__':
    main()