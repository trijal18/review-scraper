# import csv
# from apify_client import ApifyClient

# def scrape_amazon_products(url, output_file="output.csv"):
#     client = ApifyClient("apify_api_9EuS7PUyq6oHZcu1x4PiUHdtXNErjq3MMvNH")
    
#     run_input = {
#         "categoryUrls": [{"url": url}],
#         "maxItemsPerStartUrl": 1000,
#         "useCaptchaSolver": False,
#         "scrapeProductVariantPrices": False,
#         "scrapeProductDetails": True,
#     }
    
#     run = client.actor("XVDTQc4a7MDTqSTMJ").call(run_input=run_input)
    
#     dataset_items = client.dataset(run["defaultDatasetId"]).iterate_items()
    
#     with open(output_file, mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         headers_written = False
        
#         for item in dataset_items:
#             if not headers_written:
#                 writer.writerow(item.keys())  # Write headers
#                 headers_written = True
#             writer.writerow(item.values())  # Write row data
    
#     print(f"Data saved to {output_file}")

# # Example usage
# scrape_amazon_products("https://www.amazon.in/s?bbn=1388921031&rh=n%3A1388921031")
