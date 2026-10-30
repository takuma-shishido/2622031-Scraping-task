import csv
import time
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup

START_URL = "https://www.musashino-u.ac.jp/"
DOMAIN = urlparse(START_URL).netloc

pages = {}  # key: URL, value: <title>の文字列
visited = set()
queue = [START_URL]

while queue:
    url = queue.pop(0)
    if url in visited:
        continue
    visited.add(url)

    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException:
        continue
    finally:
        time.sleep(1)  # 負荷軽減

    if response.status_code != 200 or "text/html" not in response.headers.get("Content-Type", ""):
        continue

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    pages[url] = soup.title.get_text(strip=True) if soup.title else ""
    print(len(pages), url, pages[url])

    for a in soup.find_all("a", href=True):
        link = urldefrag(urljoin(url, a["href"]))[0]
        if urlparse(link).netloc == DOMAIN and link not in visited:
            queue.append(link)

with open("sitemap.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["url", "title"])
    for url, title in pages.items():
        writer.writerow([url, title])
