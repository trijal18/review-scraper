from time import sleep
from random import random
import pandas as pd
import requests
from tqdm import tqdm  # ✅ Use standard tqdm (not notebook version)
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs

# Constants
BASE_URL = 'https://www.flipkart.com/'
SEARCH_QUERY = "headphones"
TOP_N_PRODUCTS = 10
REVIEW_PAGES_TO_SCRAPE_FROM_PER_PRODUCT = 100  # 10 Reviews per page

def get_popular_product_titles_and_urls(search_query: str, popular_products_count_limit: int = None):
    # search_url = f"{BASE_URL}search?q={search_query}&sort=popularity"
    search_url="https://www.flipkart.com/headset/pr?sid=fcn&otracker=categorytree"
    search_response = requests.get(search_url)
    
    search_html_soup = BeautifulSoup(search_response.content, 'html.parser')
    search_results_products = search_html_soup.find_all('div', attrs={'class': '_4ddWXP'})

    product_titles, product_urls = [], []

    for product in tqdm(search_results_products, desc="Fetching Products"):
        ad_mention_subrow = product.find("div", attrs={"class": "_4HTuuX"})

        if not ad_mention_subrow:  # Not an ad
            title_mention_subrow = product.find("a", attrs={"class": "s1Q9rs"})

            product_title = title_mention_subrow["title"]
            product_relative_url = title_mention_subrow["href"]
            product_url = urljoin(BASE_URL, product_relative_url)

            parsed_url = urlparse(product_url)
            parsed_url_path = parsed_url.path.split("/")
            parsed_url_path[2] = "product-reviews"
            parsed_url_modified = parsed_url._replace(path="/".join(parsed_url_path))
            product_url = parsed_url_modified.geturl()

            product_titles.append(product_title)
            product_urls.append(product_url)

            if popular_products_count_limit and len(product_titles) >= popular_products_count_limit:
                break

    return product_titles, product_urls

product_titles, product_urls = get_popular_product_titles_and_urls(SEARCH_QUERY, TOP_N_PRODUCTS)

dataset = []

for idx, url in enumerate(tqdm(product_urls, desc='Processing Products')):
    for i in tqdm(range(1, REVIEW_PAGES_TO_SCRAPE_FROM_PER_PRODUCT + 1), desc="Scraping Reviews", leave=False):
        parsed = urlparse(url)
        pid = parse_qs(parsed.query).get('pid', [''])[0]
        URL = f"{url}&page={i}"

        r = requests.get(URL)
        sleep(random())  # Avoid rate-limiting
        soup = BeautifulSoup(r.content, 'html.parser')

        rows = soup.find_all('div', attrs={'class': 'col _2wzgFH K0kLPL'})

        for row in rows:
            sub_row = row.find_all('div', attrs={'class': 'row'})

            rating = sub_row[0].find('div').text.strip()
            summary = sub_row[0].find('p').text.strip()
            review = sub_row[1].find_all('div')[2].text.strip()

            location = ""
            location_row = sub_row[3].find('p', attrs={'class': '_2mcZGG'})
            if location_row:
                location_parts = location_row.find_all('span')
                if len(location_parts) >= 2:
                    location = "".join(location_parts[1].text.split(",")[1:]).strip()

            date = sub_row[3].find_all('p', attrs={'class': '_2sc7ZR'})[1].text.strip()

            sub_row_2 = row.find_all('div', attrs={'class': '_1e9_Zu'})[0].find_all('span', attrs={'class': '_3c3Px5'})
            upvotes = sub_row_2[0].text.strip()
            downvotes = sub_row_2[1].text.strip()

            dataset.append({
                'product_id': pid,
                'product_title': product_titles[idx],
                'rating': rating,
                'summary': summary,
                'review': review,
                'location': location,
                'date': date,
                'upvotes': upvotes,
                'downvotes': downvotes
            })

df = pd.DataFrame(dataset)

# ✅ Fixed pd.option_context: Use `None` instead of `-1`
with pd.option_context('display.max_colwidth', None):
    print(df.head(5))
    print(df.tail(5))
