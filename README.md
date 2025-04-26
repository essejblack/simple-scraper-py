# Simple Website Scraper

A simple Python script that uses the **BeautifulSoup (BS4)** library to scrape and extract all the links (URLs) from a given website.

## Features

- Scrapes all links (anchor tags) from a website.
- Simple and easy to use.
- Supports any website URL for extracting links.

## Technologies

- Python 3.x
- BeautifulSoup (for scraping the website)
- Requests (for making HTTP requests)

## Setup and Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries:

```bash
pip install beautifulsoup4 requests
```
3. Update the script with the target URL (e.g., bbc.com).
4. Run the script:
```
python main.py
```
The script will scrape the website and print all the links found on the page.

Note: Ensure you have permission to scrape the website. Some websites may block scraping attempts.
