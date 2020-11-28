"""
Prerequisite
    - python installed on your machine
    - basic programming knowledge of python and web scapping.
    - Motivation & desire to learn something new, 

    that's all folks, let's get started.

first install requests and bs4 packages using command mentione below.
    1. open command prompt
    2. pip install requests bs4
    
"""
import requests
from bs4 import BeautifulSoup

#code
def AmazonFetcher(URL):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

    page = requests.get(URL, headers= headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text().strip()
    converted_price = price[2:]

    return(converted_price, title)
