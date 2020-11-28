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
    img = soup.find(id="landingImage")
    # print(img)
    image_need = soup.find('data-old-hires').get_text()
    print(image_need)
    # images = soup.find_all('img', src=True)
    # print("Number of images:",len(images))
    # for image in images:
    #     print(image)

    # image_need = [x['src'] for x in images]
    # for image in image_need:
    #     print(image)
    

URL = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5S1NT7/ref=sr_1_3?dchild=1&keywords=iphone+12&qid=1606061094&sr=8-3"
AmazonFetcher(URL)

    
