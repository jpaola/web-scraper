import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Custom headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Store all scraped books
books = []

# Scrape first 5 pages
for page in range(1, 6):
    url = base_url.format(page)
    print(f"Scraping page {page}...")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()

        books.append({
            'Title': title,
            'Price': price,
            'Availability': availability
        })

    # Delay between requests to be polite
    time.sleep(2)

# Save to Excel
df = pd.DataFrame(books)
df.to_excel("scraped_books.xlsx", index=False)

print("Done! Data saved to scraped_books.xlsx")