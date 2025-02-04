import requests
from bs4 import BeautifulSoup
import pandas as pd

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

def get_reviews(soup):
    # review_elements = soup.select("div.review")
    reviews = soup.find_all('li', class_='review', attrs={'data-hook': 'review'})
    print(reviews)

    scraped_reviews = []

    for review in reviews:
        r_author_element = review.select_one("span.a-profile-name")
        r_author = r_author_element.text if r_author_element else None

        r_rating_element = review.select_one("i.review-rating")
        r_rating = r_rating_element.text.replace("out of 5 stars", "") if r_rating_element else None

        r_title_element = review.select_one("a.review-title")
        r_title_span_element = r_title_element.select_one("span:not([class])") if r_title_element else None
        r_title = r_title_span_element.text if r_title_span_element else None

        r_content_element = review.select_one("span.review-text")
        r_content = r_content_element.text if r_content_element else None

        r_date_element = review.select_one("span.review-date")
        r_date = r_date_element.text if r_date_element else None

        r_verified_element = review.select_one("span.a-size-mini")
        r_verified = r_verified_element.text if r_verified_element else None

        r_image_element = review.select_one("img.review-image-tile")
        r_image = r_image_element.attrs["src"] if r_image_element else None

        r = {
            "author": r_author,
            "rating": r_rating,
            "title": r_title,
            "content": r_content,
            "date": r_date,
            "verified": r_verified,
            "image_url": r_image
        }

        scraped_reviews.append(r)

    return scraped_reviews

def main():
    search_url = "https://www.amazon.in/MENHOOD-Grooming-Multi-Purpose-Rechargeable-Waterproof/dp/B0C74NWR9Z/?_encoding=UTF8&pd_rd_w=TJ4Mn&content-id=amzn1.sym.1ce8e3fb-9b57-4463-ab50-b0cee17dda4d&pf_rd_p=1ce8e3fb-9b57-4463-ab50-b0cee17dda4d&pf_rd_r=BT3QPSPM0AQ1PJCGJVVB&pd_rd_wg=9hrJC&pd_rd_r=d23dd72f-ad47-4085-9948-fe9f5b8c9d9c&ref_=pd_hp_d_btf_LPDEALS&th=1"
    soup = get_soup(search_url)
    data = get_reviews(soup)
    df = pd.DataFrame(data=data)

    df.to_csv("amz.csv")

if __name__ == '__main__':
    main()