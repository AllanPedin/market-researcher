import pandas as pd
import argparse
from random import randint
import time
import os
from dotenv import load_dotenv
load_dotenv()
from googleapiclient.discovery import build

def check_websites_for_terms(csv_file, search_terms):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Ensure the DataFrame has a 'Website' column
    if 'Website' not in df.columns:
        print("The CSV file must contain a 'Website' column.")
        return
    
    # Create new columns for each search term
    for term in search_terms:
        df[f'PagesWith_{term}'] = 0
    
    # Initialize the Custom Search API client
    api_key = os.environ.get('GOOGLE_API_KEY')
    print(f"API_KEY {api_key}")
    cse_id = "035dccbea6cac4745"  # Replace with your Custom Search Engine ID
    service = build("customsearch", "v1", developerKey=api_key)
    
    # Loop through each website and perform Google searches
    for index, row in df.iterrows():
        website = row['Website']
        
        for term in search_terms:
            try:
                query = f"site:{website} {term}"
                
                # Perform the Google search
                res = service.cse().list(q=query, cx=cse_id).execute()
                count = res['searchInformation']['totalResults']
                
                # Update the DataFrame
                df.at[index, f'PagesWith_{term}'] = count
                
                print(f"Processed {website}. Found {count} pages containing '{term}'.")
                
                # Introduce a delay
                time.sleep(2)
                
            except Exception as e:
                print(f"An error occurred: {e}")
                
                # Save the DataFrame to a new CSV file
                df.to_csv("output_with_page_counts.csv", index=False)
                
                return
    df.to_csv("output_with_page_counts.csv", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check company websites for specific terms.')
    parser.add_argument('terms', type=str, nargs='+', help='The terms to search for.')
    
    args = parser.parse_args()
    
    csv_file = "company_websites.csv"  # Replace with the path to your CSV file
    search_terms = args.terms  # The terms are now taken from the command-line arguments
    
    check_websites_for_terms(csv_file, search_terms)
