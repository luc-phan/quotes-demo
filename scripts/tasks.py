import os

import requests
from bs4 import BeautifulSoup
from invoke import task, context
from dotenv import load_dotenv

load_dotenv()

# --- CONFIGURATION ---
URL_BACKEND = "http://127.0.0.1:8000/api/quotes/"
URL_SOURCE = "https://quotes.toscrape.com"
TOKEN = os.getenv("DJANGO_API_TOKEN")

# --- INTERNAL LOGIC ---


def _get_headers():
    return {
        "Authorization": f"Token {TOKEN}",
        "Content-Type": "application/json"
    }


# --- EXPOSED TASKS (Invoke) ---


@task
def check_token(c: context.Context):
    """Verify connectivity and token."""
    if not TOKEN:
        print("Error: TOKEN is missing.")
        return
    res = requests.get(URL_BACKEND, headers=_get_headers())
    print(f"Status: {res.status_code}")


@task
def crawl(c: context.Context):
    """Scrape and upload quotes."""
    print("Starting extraction...")
    res = requests.get(URL_SOURCE)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    for q in soup.find_all('div', class_='quote'):
        data = {
            "text": q.find('span', class_='text').get_text(),
            "author": q.find('small', class_='author').get_text()
        }
        post_res = requests.post(URL_BACKEND, json=data, headers=_get_headers())
        print(f"Upload {data['author']}: {post_res.status_code}")
