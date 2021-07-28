import requests
import asyncio
from bs4 import BeautifulSoup
import time
s = time.time()
results = []

#---------------------- A 파트 ------------------------
async def getpage(url):
    req = await loop.run_in_executor(None, requests.get, url)
    html = req.text
    soup = await loop.run_in_executor(None, BeautifulSoup, html, 'lxml')
    return soup

#---------------------- B 파트 ------------------------
async def main():
    urls = [
        "https://wp.me/p9x2W1-x",
        "https://wp.me/p9x2W1-w",
        "https://wp.me/p9x2W1-t",
        "https://wp.me/p9x2W1-q",
        "https://wp.me/p9x2W1-p",
        "https://wp.me/p9x2W1-j",
        "https://wp.me/p9x2W1-h"
    ]

    fts = [asyncio.ensure_future(getpage(u)) for u in urls]
    r = await asyncio.gather(*fts)
    global results
    results = r

#---------------------- C 파트 ------------------------
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
e = time.time()
print(e)



#https://wikidocs.net/21046
