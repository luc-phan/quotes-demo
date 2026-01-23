import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Configuration
SOURCE_URL = "https://quotes.toscrape.com"
API_URL = "http://127.0.0.1:8000/api/quotes/"
TOKEN = os.getenv("DJANGO_API_TOKEN")


def fetch_quotes():
    """Scrape quotes from the target website."""
    print(f"Fetching quotes from {SOURCE_URL}...")
    response = requests.get(SOURCE_URL)
    response.raise_for_status() # Raise error if site is down
    
    soup = BeautifulSoup(response.text, 'html.parser')
    extracted_data = []

    for quote_div in soup.find_all('div', class_='quote'):
        text = quote_div.find('span', class_='text').get_text()
        author = quote_div.find('small', class_='author').get_text()
        extracted_data.append({
            "text": text,
            "author": author
        })
    
    return extracted_data


def upload_to_backend(data):
    """Send extracted data to the Django API."""
    if not TOKEN:
        print("Error: API Token missing.")
        return

    headers = {
        "Authorization": f"Token {TOKEN}",
        "Content-Type": "application/json"
    }

    for item in data:
        response = requests.post(API_URL, json=item, headers=headers)
        if response.status_code == 201:
            print(f"Successfully uploaded: {item['author']}")
        else:
            print(f"Failed to upload: {item['author']} - {response.status_code}")


if __name__ == "__main__":
    try:
        quotes = fetch_quotes()
        print(f"Extracted {len(quotes)} quotes.")
        upload_to_backend(quotes)
    except Exception as e:
        print(f"An error occurred: {e}")
