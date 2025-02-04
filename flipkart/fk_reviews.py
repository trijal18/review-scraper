# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd

# # BASE_URL = "https://www.flipkart.com/aroma-nb121-pro-pods-upto-40-hours-playtime-type-c-fast-charging-dual-pairing-earbuds-bluetooth/product-reviews/itm911b47c91c5dd?pid=ACCH77MF4NYVHZTE&lid=LSTACCH77MF4NYVHZTETGQDWP&marketplace=FLIPKART&page="
# # HEADERS = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# # }

# # def get_reviews(url):
# #     response = requests.get(url, headers=HEADERS)
# #     if response.status_code != 200:
# #         print(f"Failed to retrieve page {url}")
# #         return []
    
# #     soup = BeautifulSoup(response.text, "html.parser")
# #     reviews = []
    
# #     review_elements = soup.find_all("div", class_="t-ZTKy")  # Flipkart review class
    
# #     for review in review_elements:
# #         reviews.append(review.get_text(strip=True))
    
# #     return reviews

# # # Collect reviews from multiple pages
# # all_reviews = []
# # for i in range(1, 7):  # Scraping first 6 pages of reviews
# #     page_url = BASE_URL + str(i)
# #     page_reviews = get_reviews(page_url)
# #     all_reviews.extend(page_reviews)

# # # Save to CSV
# # df = pd.DataFrame(all_reviews, columns=["Reviews"])
# # df.to_csv("flipkart_reviews.csv", index=False)

# # print("Scraping completed. Data saved to flipkart_reviews.csv")

# ## Product url
# # https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/product-reviews/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&lid=LSTMOBGQFX672GDDQAQSSIAM2&marketplace=FLIPKART
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from urllib.parse import urlparse, parse_qs


# def review_url(product_url):
#     # Parse the URL
#     parsed_url = urlparse(product_url)
    
#     # Split the path to extract the product ID
#     path_parts = parsed_url.path.split('/')
#     if 'p' in path_parts:
#         product_index = path_parts.index('p') + 1
#         if product_index < len(path_parts):
#             product_id = path_parts[product_index]
#         else:
#             raise ValueError("Product ID not found in the URL.")
#     else:
#         raise ValueError("Invalid product URL format.")
    
#     # Extract query parameters
#     query_params = parse_qs(parsed_url.query)
#     pid = query_params.get('pid', [None])[0]
#     lid = query_params.get('lid', [None])[0]
    
#     if not pid or not lid:
#         raise ValueError("Required query parameters 'pid' or 'lid' are missing.")
    
#     # Construct the review URL
#     review_url = f"https://www.flipkart.com{parsed_url.path.replace('/p/', '/product-reviews/')}"
#     review_url += f"?pid={pid}&lid={lid}"
#     review_url=review_url+"&page="
#     return review_url

# # User-Agent and Accept-Language headers
# headers = {
#     'User-Agent': 'Use your own user agent',
#     'Accept-Language': 'en-us,en;q=0.5'
# }
# customer_names = []
# review_title = []
# ratings = []
# comments = []

# for i in range(1, 10):
#     # Construct the URL for the current page
#     url = "https://www.flipkart.com/boat-airdopes-supreme-w-4-mics-ai-enx-tech-50-hrs-playback-multi-point-connectivity-bluetooth/p/itm47a93966ad11e?pid=ACCGWU2ABQ3EAUM8&lid=LSTACCGWU2ABQ3EAUM8BCMNOE&marketplace=FLIPKART&store=fcn&otracker=browse&fm=organic&iid=94533476-eb80-4deb-932e-40afbd4f993c.ACCGWU2ABQ3EAUM8.SEARCH&ppt=None&ppn=None&ssid=jjjvvw3ye80000001738593424968"

#     url=str(review_url(url))
#     url=url+f"{i}"

#     print(url)
    
#     # Send a GET request to the page
#     page = requests.get(url, headers=headers)

#     # Parse the HTML content
#     soup = BeautifulSoup(page.content, 'html.parser')

#     # Extract customer names
#     names = soup.find_all('p', class_='_2NsDsF AwS1CA')
#     for name in names:
#         customer_names.append(name.get_text())

#     # Extract review titles
#     title = soup.find_all('p', class_='z9E0IG')
#     for t in title:
#         review_title.append(t.get_text())

#     # Extract ratings
#     rat = soup.find_all('div', class_='XQDdHH Ga3i8K')
#     for r in rat:
#         rating = r.get_text()
#         if rating:
#             ratings.append(rating)
#         else:
#             ratings.append('0')  # Replace null ratings with 0

#     # Extract comments
#     cmt = soup.find_all('div', class_='ZmyHeo')
#     for c in cmt:
#         comment_text = c.div.div.get_text(strip=True)
#         comments.append(comment_text)

# # Ensure all lists have the same length
# min_length = min(len(customer_names), len(review_title), len(ratings), len(comments))
# customer_names = customer_names[:min_length]
# review_title = review_title[:min_length]
# ratings = ratings[:min_length]
# comments = comments[:min_length]

# # Create a DataFrame from the collected data
# data = {
#     'Customer Name': customer_names,
#     'Review Title': review_title,
#     'Rating': ratings,
#     'Comment': comments
# }

# df = pd.DataFrame(data)

# print(len(customer_names))
# print(len(review_title))
# print(len(ratings))
# print(len(comments))
# customer_names
# ## comments
# import pandas as pd
# data = {
#     'Customer Name': customer_names,
#     'Review Title': review_title,
#     'Rating': ratings,
#     'Comment': comments
# }


# df = pd.DataFrame(data)
# # df['Rating'].fillna(0, inplace=True)

# # Save the DataFrame to a CSV file
# df.to_csv('test.csv', index=False)
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse, parse_qs

# Function to construct the review URL from the product URL
def construct_review_url(product_url):
    parsed_url = urlparse(product_url)
    query_params = parse_qs(parsed_url.query)
    pid = query_params.get('pid', [None])[0]
    lid = query_params.get('lid', [None])[0]
    
    if not pid or not lid:
        raise ValueError("Required query parameters 'pid' or 'lid' are missing.")
    
    review_url = f"https://www.flipkart.com{parsed_url.path.replace('/p/', '/product-reviews/')}"
    review_url += f"?pid={pid}&lid={lid}&page="
    return review_url

# Function to scrape reviews from the review URL
def scrape_reviews(product_url,output_path, max_pages=10):
    review_base_url = construct_review_url(product_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-us,en;q=0.5'
    }
    
    customer_names, review_titles, ratings, comments = [], [], [], []
    
    for i in range(1, max_pages + 1):
        url = review_base_url + str(i)
        print(f"Scraping page: {i} -> {url}")
        
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # Extract data
        names = soup.find_all('p', class_='_2NsDsF AwS1CA')
        titles = soup.find_all('p', class_='z9E0IG')
        rats = soup.find_all('div', class_='XQDdHH Ga3i8K')
        cmts = soup.find_all('div', class_='ZmyHeo')
        
        customer_names.extend([name.get_text() for name in names])
        review_titles.extend([t.get_text() for t in titles])
        ratings.extend([r.get_text() if r.get_text() else '0' for r in rats])
        comments.extend([c.div.div.get_text(strip=True) for c in cmts if c.div and c.div.div])
    
    # Ensure all lists have the same length
    min_length = min(len(customer_names), len(review_titles), len(ratings), len(comments))
    customer_names = customer_names[:min_length]
    review_titles = review_titles[:min_length]
    ratings = ratings[:min_length]
    comments = comments[:min_length]
    
    # Create a DataFrame
    data = {
        'Customer Name': customer_names,
        'Review Title': review_titles,
        'Rating': ratings,
        'Comment': comments
    }
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    
    # return df

# Example usage
product_url = "https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/product-reviews/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&lid=LSTMOBGQFX672GDDQAQSSIAM2&marketplace=FLIPKART"
scrape_reviews(product_url,"ddd.csv", max_pages=15)

