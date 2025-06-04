import html.parser
import requests
from bs4 import BeautifulSoup
import threading
import html
from concurrent.futures import ThreadPoolExecutor
import time

urls = ["https://example.com" for i in range(50)]
print(urls)

def fetch_data(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(f"Fetched {len(soup.getText())} from {url}\n")
    return "Done"

threads = []

t = time.time()
for url in urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Done within: {time.time() - t}")

t = time.time()
with ThreadPoolExecutor(max_workers=50) as tpe:
    results = tpe.map(fetch_data, urls)

# for r in results:
#     print(r)

print(time.time() - t)