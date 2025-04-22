import requests
from bs4 import BeautifulSoup
import os

url = "http://www.bbc.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
results = soup.find_all("a")

urls = set()
for r in results:
    link = r.get("href")
    if not "https" in link:
        link = "https://www.bbc.com" + link
    urls.add(link)
print(urls)