from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib import parse
import re
def getPictureLink(el):
    try:
        src = el.find_element(By.CLASS_NAME,"K0PDV").get_attribute("style")
        return parse.unquote(src[src.find("src=")+4:-3])
    except:
        return None

nums = []
fin=[]
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://m.map.naver.com/search2/search.naver?query=마라탕#/list")

try:
    for i in range(1, 75 + 1):
        csss = "#ct > div.search_listview._content._ctList > ul > li:nth-child(%d)" % i
        search = driver.find_element(By.CSS_SELECTOR, csss).get_attribute("data-sid")
        nums.append(search)
except:
    pass
for i in nums[:10]:
    next_url = "https://m.place.naver.com/restaurant/%s/menu/list" % i
    driver.get(next_url)
    time.sleep(0.5)
    menus = []
    info={}
    info["link"]="https://map.naver.com/v5/entry/place/"+i
    info["name"]=driver.find_element(By.CLASS_NAME, "Fc1rA").text
    info["star"]=driver.find_element(By.TAG_NAME, "em").text
    if (len(driver.find_elements(By.CLASS_NAME,"r8zp9"))==0):
        for price, names in zip(driver.find_elements(By.CLASS_NAME, "SSaNE"),
                                         driver.find_elements(By.CLASS_NAME, "Sqg65")):
            menus.append([names.text, price.text,None])
    else:
        for price, names, picture in zip(driver.find_elements(By.CLASS_NAME, "SSaNE"),   driver.find_elements(By.CLASS_NAME, "Sqg65"),driver.find_elements(By.CLASS_NAME,"r8zp9")):
            menus.append([names.text, price.text, getPictureLink(picture)])
    info["menus"]=menus
    fin.append(info)


for i in fin:
    print(i)
# 크롭 웹페이지를 닫음]
driver.close()
