import csv
import threading
from amz_api import export_to_csv

def export(url,o):
    print(f"{url}")
    print(f"{o}")

def read_csv_and_process(file_path):
    threads = []
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if it exists
        
    #     for index, row in enumerate(reader):  # Use enumerate to get the iterator
    #         if not row:  
    #             continue  # Skip empty rows

    #         output_path=f"amazon/headphones/{index}.csv"

    #         url = row[1]  # Take the first column as URL
    #         thread = threading.Thread(target=export_to_csv, args=(url, output_path))
    #         # thread = threading.Thread(target=export, args=(url, output_path))
    #         thread.start()
    #         threads.append(thread)

    # for thread in threads:
    #     thread.join()

        for index, row in enumerate(reader):  # Use enumerate to get the iterator
            if not row:  
                continue  # Skip empty rows

            output_path=f"amazon/watchs/{index}.csv"

            url = row[1]  # Take the first column as URL
            export_to_csv(url,output_path)

# Example usage
read_csv_and_process("amz_links_3.csv")
