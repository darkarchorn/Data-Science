'''
Real-world Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to
fetch web pages. These tasks are I/O-bound because they spend a lot of
time waiting for responses fro servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently
'''
import sys

# URLs
# https://python.langchain.com/v0.2/docs/introduction/
# https://python.langchain.com/v0.2/docs/conccepts/
# https://python.langchain.com/v0.2/docs/tutorials/

print(sys.prefix)


import threading
import requests
from bs4 import BeautifulSoup 

urls = ["https://python.langchain.com/v0.2/docs/introduction/",
"https://python.langchain.com/v0.2/docs/conccepts/",
"https://python.langchain.com/v0.2/docs/tutorials/"]

def fetch_content(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content,"html.parser")
    print(f'Fetched: {(len(soup.text))} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content(url=url), args=(url, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All pages are fetched")