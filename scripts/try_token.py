import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

URL = "http://127.0.0.1:8000/api/quotes/"
TOKEN = os.getenv("DJANGO_API_TOKEN")


def run_connection_trial():
    if not TOKEN:
        print("Error: DJANGO_API_TOKEN environment variable is missing.")
        return

    headers = {
        "Authorization": f"Token {TOKEN}",
        "Content-Type": "application/json"
    }

    # Data that will actually be saved in your database
    payload = {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    }

    try:
        print(f"Sending trial request to {URL}...")
        response = requests.post(URL, json=payload, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 201:
            print("Successfully injected data into the database.")
        else:
            print(f"Trial failed: {response.text}")

    except requests.exceptions.ConnectionError:
        print("Connection Error: Is the Django server running?")


if __name__ == "__main__":
    run_connection_trial()
