import pandas as pd
import argparse
from random import randint
import time
from googlesearch import search

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
    
    # Loop through each website and perform Google searches
    for index, row in df.iterrows():
        website = row['Website']
        
        for term in search_terms:
            try:

                query = f"site:{website} {term}"
                
                # Perform the Google search
                search_results = search(query, num_results=100)
                
                # Count the number of pages from the website that contain the term
                count = sum(website in result['url'] for result in search_results)
                
                # Update the DataFrame
                df.at[index, f'PagesWith_{term}'] = count
                
                print(f"Processed {website}. Found {count} pages containing '{term}'.")

                # Introduce a delay
                time.sleep(randint(30,40))
            except Exception as e:
                print(f"An error occurred: {e}")
                
                # Save the DataFrame to a new CSV file
                df.to_csv("output_with_page_counts.csv", index=False)
                
                return
    # Save the DataFrame to a new CSV file
    df.to_csv("output_with_page_counts.csv", index=False)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check company websites for specific terms.')
    parser.add_argument('terms', type=str, nargs='+', help='The terms to search for.')
    
    args = parser.parse_args()
    
    csv_file = "company_websites.csv"  # Replace with the path to your CSV file
    search_terms = args.terms  # The terms are now taken from the command-line arguments
    
    check_websites_for_terms(csv_file, search_terms)
