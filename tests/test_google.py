import requests
import time
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get API Key from env file
API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX")

# Search query: targeting Facebook pages in Bangladesh with relevant keywords
QUERY = '("student club" OR "student association") site:facebook.com bangladesh'  # Simplified for testing

# Base URL
base_url = "https://www.googleapis.com/customsearch/v1"

# Store all results here
results = []

# Fetch up to 30 results (3 pages of 10 results each)
for start in range(1, 11, 10):  # Just 1 page for now
    print(f"\n🔍 Fetching results {start} to {start + 9}...")

    params = {
        "key": API_KEY,
        "cx": CX,
        "q": QUERY,
        "start": start
    }

    response = requests.get(base_url, params=params)
    # print("⚙️ Full URL:", response.url)  # See full request
    data = response.json()
    # print("📦 Raw response:", data)  # Debug output

    if "items" not in data:
        print("⚠️ No results. Check your CX config or quota.")
        break

    for item in data["items"]:
        title = item.get("title", "No Title")
        link = item.get("link", "No Link")
        snippet = item.get("snippet", "No Description")

        print(f"\n📌 Title: {title}\n🔗 Link: {link}\n📝 Snippet: {snippet}")
        results.append((title, link, snippet))

    time.sleep(1)

print(f"\n✅ Total results fetched: {len(results)}")