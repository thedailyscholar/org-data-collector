# Test script for Google Search api

import requests
import time
import os
import csv
from dotenv import load_dotenv

# Load env variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX")

CSV_FILE = "results.csv"

# -------------------------------
# Function 1: Fetch Results
# -------------------------------
def fetch_results(query, max_pages=5, start_index=1):
    """
    Fetch results for a given query.
    Stops early if no more results are returned.
    """
    base_url = "https://www.googleapis.com/customsearch/v1"
    results = []

    for page in range(max_pages):  # loop pages
        start = start_index + (page * 10)  # 10 results per page
        print(f"\n🔍 Fetching results {start} to {start + 9}...")

        params = {
            "key": API_KEY,
            "cx": CX,
            "q": query,
            "start": start,
            "gl": "bd",
            "lr": "lang_en"
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if "items" not in data:  # No more results
            print("⚠️ No more results or quota exceeded. Stopping early.")
            break

        for item in data["items"]:
            title = item.get("title", "No Title")
            link = item.get("link", "No Link")
            snippet = item.get("snippet", "No Description")
            print(f"\n📌 Title: {title}\n🔗 Link: {link}\n📝 Snippet: {snippet}")
            results.append((title, link, snippet))

        time.sleep(1)  # avoid hitting rate limits

    return results

# -------------------------------
# Function 2: Save to CSV
# -------------------------------
def save_to_csv(results, filename=CSV_FILE):
    existing_links = set()
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) >= 2:
                    existing_links.add(row[1])  # link column

    new_entries = [r for r in results if r[1] not in existing_links]

    if new_entries:
        file_exists = os.path.exists(filename)
        with open(filename, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Title", "Link", "Snippet"])
            writer.writerows(new_entries)
        print(f"✅ Saved {len(new_entries)} new results to {filename}")
    else:
        print("ℹ️ No new results to save (all duplicates).")

# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    QUERIES = [
        # Universities
        '("DU" OR "University of Dhaka") ("student club" OR "debating club" OR "cultural club" OR "business club" OR "photography club" OR "volunteer club") site:facebook.com',
        '("BUET" OR "Bangladesh University of Engineering and Technology") ("student club" OR "debating club" OR "cultural club" OR "science club" OR "robotics club") site:facebook.com',
        '("NSU" OR "North South University") ("student club" OR "business club" OR "cultural club" OR "debating club" OR "photography club" OR "MUN") site:facebook.com',
        '("BRACU" OR "BRAC University") ("student club" OR "business club" OR "cultural club" OR "debating club" OR "volunteer club") site:facebook.com',
        '("IUB" OR "Independent University Bangladesh") ("student club" OR "environment club" OR "cultural club" OR "film club" OR "photography club") site:facebook.com',
        '("AIUB" OR "American International University Bangladesh") ("student club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("BUP" OR "Bangladesh University of Professionals") ("student association" OR "cultural club" OR "debating club" OR "volunteer club") site:facebook.com',
        '("MIST" OR "Military Institute of Science and Technology") ("student club" OR "debating club" OR "cultural club" OR "robotics club") site:facebook.com',
        '("EWU" OR "East West University") ("student club" OR "cultural club" OR "debating club" OR "volunteer club") site:facebook.com',
        '("UIU" OR "United International University") ("student club" OR "cultural club" OR "debating club" OR "business club") site:facebook.com',
        '("DIU" OR "Daffodil International University") ("student club" OR "cultural club" OR "debating club" OR "photography club") site:facebook.com',

        # Colleges
        '("Notre Dame College") ("debating club" OR "cultural club" OR "volunteer club" OR "business club") site:facebook.com',
        '("Holy Cross College") ("debating club" OR "cultural club" OR "volunteer club") site:facebook.com',
        '("Viqarunnisa Noon College") ("debating club" OR "cultural club" OR "volunteer club" OR "sports club") site:facebook.com',
        '("Adamjee Cantonment College") ("debating club" OR "cultural club" OR "photography club" OR "science club") site:facebook.com',
        '("Rajuk College" OR "Rajuk Uttara Model College") ("debating club" OR "science club" OR "cultural club" OR "sports club") site:facebook.com',
        '("Dhaka College") ("debating club" OR "cultural club" OR "volunteer club") site:facebook.com',

        # Schools
        '("Scholastica") ("science club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("Sunbeams School") ("science club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("Maple Leaf International School") ("science club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("Sunnydale School") ("science club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("Viqarunnisa Noon School") ("science club" OR "cultural club" OR "debating club") site:facebook.com',
        '("St Joseph School Dhaka") ("science club" OR "cultural club" OR "debating club" OR "sports club") site:facebook.com',
        '("St Gregory’s School") ("science club" OR "cultural club" OR "debating club") site:facebook.com'
    ]

    for query in QUERIES:
        print(f"\n🚀 Running query: {query}")
        results = fetch_results(query, max_pages=5, start_index=1)  # change max page as required
        print(f"\n✅ Total fetched for this query: {len(results)}")
        save_to_csv(results)
