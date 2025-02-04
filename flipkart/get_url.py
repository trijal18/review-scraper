from urllib.parse import urlparse, parse_qs

def review_url(product_url):
    # Parse the URL
    parsed_url = urlparse(product_url)
    
    # Split the path to extract the product ID
    path_parts = parsed_url.path.split('/')
    if 'p' in path_parts:
        product_index = path_parts.index('p') + 1
        if product_index < len(path_parts):
            product_id = path_parts[product_index]
        else:
            raise ValueError("Product ID not found in the URL.")
    else:
        raise ValueError("Invalid product URL format.")
    
    # Extract query parameters
    query_params = parse_qs(parsed_url.query)
    pid = query_params.get('pid', [None])[0]
    lid = query_params.get('lid', [None])[0]
    
    if not pid or not lid:
        raise ValueError("Required query parameters 'pid' or 'lid' are missing.")
    
    # Construct the review URL
    review_url = f"https://www.flipkart.com{parsed_url.path.replace('/p/', '/product-reviews/')}"
    review_url += f"?pid={pid}&lid={lid}"
    review_url=review_url+"&page="
    return review_url

# Example usage:
product_url = "https://www.flipkart.com/aroma-nb137-dive-upto-60-hours-playtime-type-c-fast-charging-dual-pairing-earbuds-bluetooth/p/itm608c337770dd2?pid=ACCH5ZD3EGCBP7G3&lid=LSTACCH5ZD3EGCBP7G3UPMYYE&marketplace=FLIPKART&store=fcn&otracker=browse&fm=organic&iid=en_JqI9nGcoET2W46EjpCg5oFJ6zOtmX0MhXlrbk41M7Bq2tmkswA_JHvyd0izymiv2udCNJteC1OUhuhHHyYR6pA%3D%3D&ppt=None&ppn=None&ssid=jjjvvw3ye80000001738593424968"
review_url = review_url(product_url)
print("Review URL:", review_url)