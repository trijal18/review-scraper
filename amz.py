import pandas as pd
import os

def drop_columns_from_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    print(f"Original data from {input_file}:")
    print(df.head())  # Print first few rows to check

    # List of columns to drop (based on the new column names)
    columns_to_drop = [
        'reviewedIn', 'userId', 'userProfileLink', 'reviewReaction', 'isVerified', 
        'isAmazonVine', 'variantAttributes', 'totalCategoryReviews', 'reviewCategoryUrl',
        'filterByRating', 'filterByKeyword', 'productAsin', 'productOriginalAsin', 
        'variantAsin', 'product', 'input', 'country', 'countryCode'
    ]

    # Drop the specified columns
    df = df.drop(columns=columns_to_drop, errors='ignore')
    print(f"Data after dropping columns for {input_file}:")
    print(df.head())  # Print first few rows after modification

    # Save the updated CSV to a new file
    df.to_csv(output_file, index=False)

def process_directory(input_dir, output_dir):
    # Check if output directory exists, create if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Loop through each file in the directory
    for filename in os.listdir(input_dir):
        # Only process CSV files
        if filename.endswith('.csv'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"watch_{filename}")
            drop_columns_from_csv(input_file, output_file)
            print(f"Processed {filename} and saved to {output_file}")

# Usage example
input_dir = r'D:\aaahhhhh\amazon-review\amazon\watchs'  # Replace with your input directory
output_dir = r'D:\aaahhhhh\amazon-review\amazon\watches'  # Replace with your desired output directory

process_directory(input_dir, output_dir)
