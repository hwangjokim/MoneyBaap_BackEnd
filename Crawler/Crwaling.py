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

def saveUniqueNumber():
    temp=[]
    f = open("unique_number.txt", 'w')
    driver.switch_to.frame("searchIframe")
    for _ in range(6):

        driver.find_element(By.CSS_SELECTOR,"span.h69bs.KvAhC.utj_r").click()
        for i in range(10):
            time.sleep(0.2)
            driver.find_element(By.XPATH,'//body').send_keys(Keys.CONTROL + Keys.END)
        print(len(driver.find_elements(By.CSS_SELECTOR, "span.place_bluelink.TYaxT")))
        for i in driver.find_elements(By.CSS_SELECTOR, "span.place_bluelink.TYaxT"):
            i.click()
            time.sleep(0.7)
            driver.switch_to.default_content()
            driver.switch_to.frame("entryIframe")
            p = re.compile("place/\d+")
            m = p.search(driver.current_url).group()
            numbers = re.sub(r'[^0-9]', '', m)
            if numbers not in temp:
                temp.append(numbers)
                f.write("%s\n" %numbers)
            driver.switch_to.default_content()
            driver.switch_to.frame("searchIframe")
        driver.find_elements(By.CSS_SELECTOR,"svg.yUtES")[1].click()
    f.close()
def loadSavingNumber():
    with open("unique_number.txt") as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines


fin=[]
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://map.naver.com/v5/search/숭실대맛집")
time.sleep(5)
nums=loadSavingNumber()


# Todo 네이버에서 주문가능 경우 체크하기

# try:
#     for i in range(1, 75 + 1):
#         csss = "#ct > div.search_listview._content._ctList > ul > li:nth-child(%d)" % i
#         search = driver.find_element(By.CSS_SELECTOR, csss).get_attribute("data-sid")
#         nums.append(search)
# except:
#     pass


for i in nums[:2]:
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
