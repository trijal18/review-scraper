import requests
import csv
from apify_client import ApifyClient

def export_to_csv(url, output_filename='output.csv'):
    try:
        client = ApifyClient("apify_api_9EuS7PUyq6oHZcu1x4PiUHdtXNErjq3MMvNH")
        run_input = {
            "productUrls": [{"url": url}],
            "maxReviews": 500,
            "sort": "helpful",
            "includeGdprSensitive": False,
            "filterByRatings": ["allStars"],
            "reviewsUseProductVariantFilter": False,
            "reviewsEnqueueProductVariants": False,
            "proxyCountry": "AUTO_SELECT_PROXY_COUNTRY",
            "scrapeProductDetails": False,
            "reviewsAlwaysSaveCategoryData": False,
            "scrapeQuickProductReviews": True,
            "deduplicateRedirectedAsins": True,
        }
        run = client.actor("R8WeJwLuzLZ6g4Bkk").call(run_input=run_input)
        
        data = list(client.dataset(run["defaultDatasetId"]).iterate_items())
        
        if not data:
            print("No data found.")
            return

        keys = data[0].keys()
        with open(output_filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        print(f"Data successfully exported to {output_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
export_to_csv('https://www.amazon.in//ZEBRONICS-Theatre-Bluetooth-Powerful-Subwoofer/dp/B0C6T54WWJ/ref=zg_bs_g_1389365031_d_sccl_28/262-4334605-4855948?psc=1')
