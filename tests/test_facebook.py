import requests
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get Access Token from env file
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")

FIELDS = "id,name,username,about,category,location,website,link,fan_count"

def get_page_info():
    url = f"https://graph.facebook.com/v23.0/{PAGE_ID}"
    params = {
        "fields": FIELDS,
        "access_token": ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)


def list_managed_pages():
    pages = []
    url = "https://graph.facebook.com/v23.0/me/"
    params = {
        "fields": "id,name",
        "access_token": ACCESS_TOKEN
    }

    response = requests.get(url, params=params)
    data = response.json()
    pages.append(data)
    print("Data", data)
    print("Pages", pages)

    if 'error' in data:
        print("Error:", data['error']['message'])
    else:
        # pages = data.get("data", [])
        if not pages:
            print("No pages found or accessible.")
        for page in pages:
            print(f"Page Name: {page['name']}")
            print(f"Page ID: {page['id']}")
            print("-----")

if __name__ == "__main__":
    # get_page_info()
    list_managed_pages()

