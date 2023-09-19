# Company Website Term Checker

## Overview

This Python script reads a list of company websites from a CSV file and checks how many pages on each website contain a specified term, according to Google search results. The results are saved to a new CSV file.

## Requirements

- Python 3.x
- `pandas`
- `googlesearch-python`

## Installation

1. Clone the repository or download the script.
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a CSV file named `company_websites.csv` with a column labeled `Website` that contains the list of company websites you want to check.

2. Run the script from the command line, passing the term you're looking for as an argument:

    ```bash
    python market_researcher.py blockchain bitcoin cryptocurrency ethereum altcoin
    ```

Replace `script_name.py` with the name of your Python script and `"blockchain"` with the term you're looking for.

## Output

The script will generate a new CSV file named `output_with_page_counts.csv`, which will contain the original list of websites along with a new column indicating the number of pages on each website that contain the specified term.
