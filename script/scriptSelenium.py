from selenium import webdriver
#import for time of sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#path for chrome web drivers
PATH = "C:/Users/chase/Projects/Micro/Scraper/chromedriver.exe"

#code
def PriceFetcher(URL):

    #adding headless mode 
    #it doesn't going to oen a window in simple words
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(PATH,options=op)

    driver.get("https://www.pricetrackers.in/")
    


    page = driver.find_element_by_id("purl")
    page.send_keys(URL)

    submit = driver.find_element_by_id("load_button")
    submit.click()

    time.sleep(1)

    avprice = driver.find_element_by_id("avgPrice").text
    maxprice = driver.find_element_by_id("maximumPrice").text
    minprice = driver.find_element_by_id("minimumPrice").text
    picsrc = driver.find_element_by_id("productImageURL")

    return(minprice, avprice, maxprice)

#driver
search_link = "https://www.amazon.in/New-Apple-iPhone-12-128GB/dp/B08L5S1NT7/ref=sr_1_3?dchild=1&keywords=iphone+12&qid=1606061094&sr=8-3"

print(PriceFetcher(search_link))

