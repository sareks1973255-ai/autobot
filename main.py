import requests
from bs4 import BeautifulSoup
import re

def search_companies(query):
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    search_url = f"https://www.google.com/search?q={query}+telefon"

    r = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text(" ")

    # Telefonlar
    phones = re.findall(r'\+?\d[\d\s\-\(\)]{7,}\d', text)

    # Telegram username
    telegrams = re.findall(r'@[\w_]+', text)

    results.append({
        "query": query,
        "phones": list(set(phones))[:10],
        "telegrams": list(set(telegrams))[:10]
    })

    return results


if __name__ == "__main__":
    q = input("Kategoriya kiriting: ")

    data = search_companies(q)

    for item in data:
        print("\n=== NATIJA ===")
        print("Qidiruv:", item["query"])

        print("\nTelefonlar:")
        for p in item["phones"]:
            print("-", p)

        print("\nTelegramlar:")
        for t in item["telegrams"]:
            print("-", t)
