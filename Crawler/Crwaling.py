import re
import time
from urllib import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


def get_picture_link(el):
    try:
        src = el.find_element(By.CLASS_NAME, "K0PDV").get_attribute("style")
        return parse.unquote(src[src.find("src=") + 4:-3])
    except:
        return None


def save_unique_number(target_locate):
    temp = []
    local_cnt=0
    driver.get("https://map.naver.com/v5/search/%s" %target_locate)
    time.sleep(5)
    f = open(target_locate+".txt", 'w')
    driver.switch_to.frame("searchIframe")
    for _ in range(6):
        driver.find_element(By.CSS_SELECTOR, "span.h69bs.KvAhC.utj_r").click()
        for i in range(10):
            time.sleep(0.2)
            driver.find_element(By.XPATH, '//body').send_keys(Keys.CONTROL + Keys.END)
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
                f.write("%s\n" % numbers)
            driver.switch_to.default_content()
            driver.switch_to.frame("searchIframe")
        driver.find_elements(By.CSS_SELECTOR, "svg.yUtES")[1].click()
    f.close()
    print()


def load_saving_number():
    with open("unique_number.txt") as f:
        lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return lines


def crawl_without_naver_order(driver, i):
    menus = []
    try:
        info = {"link": "https://map.naver.com/v5/entry/place/" + i,
                "name": driver.find_element(By.CLASS_NAME, "Fc1rA").text,
                "star": driver.find_element(By.TAG_NAME, "em").text}
    except:
        return None
    driver.implicitly_wait(0)
    if len(driver.find_elements(By.CLASS_NAME, "r8zp9")) == 0:
        for price, names in zip(driver.find_elements(By.CLASS_NAME, "SSaNE"),
                                driver.find_elements(By.CLASS_NAME, "Sqg65")):
            menus.append([names.text, price.text, None])
    else:
        for price, names, picture in zip(driver.find_elements(By.CLASS_NAME, "SSaNE"),
                                         driver.find_elements(By.CLASS_NAME, "Sqg65"),
                                         driver.find_elements(By.CLASS_NAME, "r8zp9")):
            menus.append([names.text, price.text, get_picture_link(picture)])
    info["menus"] = menus
    return info


def crawl_with_naver_order(driver, i):
    menus = []
    driver.get("https://m.place.naver.com/restaurant/%s/home" %i)
    driver.implicitly_wait(1)

    info = {"link": "https://map.naver.com/v5/entry/place/" + i,
            "name": driver.find_element(By.CLASS_NAME, "Fc1rA").text,
            "star": driver.find_element(By.TAG_NAME, "em").text}
    driver.get("https://m.place.naver.com/restaurant/%s/menu/list" % i)
    time.sleep(0.8)
    #Todo : 이미지 리스트 구분해서 menus에 append 한 뒤에 info return
    driver.implicitly_wait(0)
    for menu in driver.find_elements(By.CLASS_NAME,"order_list_item"):
        if len(menu.find_elements(By.CSS_SELECTOR,".img_box.no_img"))==0:
            name=menu.find_element(By.CLASS_NAME,"tit").text
            price=menu.find_element(By.CLASS_NAME,"price").text
            img_src=get_picture_link_with_naver(menu)
            menus.append([name,price,img_src])
        else:
            name = menu.find_element(By.CLASS_NAME, "tit").text
            price = menu.find_element(By.CLASS_NAME, "price").text
            menus.append([name, price, None])

    #refactoring
    # for name,price, picture in zip(driver.find_elements(By.CLASS_NAME,"tit"),driver.find_elements(By.CLASS_NAME,"price"),driver.find_elements(By.CLASS_NAME,"info_img")):
    #     menus.append([name.text,price.text,get_picture_link_with_naver(picture)])
    info["menus"]=menus
    return info

def get_picture_link_with_naver(pic):
    try:
        img_src = pic.find_element(By.CLASS_NAME, "img").get_attribute("src")
        img_src = img_src[:img_src.find("?")]
        return img_src
    except:
        return None

def get_result():
    do_crawl()
    driver.close()
    return fin

def do_crawl():
    nums = load_saving_number()
    count = 0
    for i in nums[:50]:
        count += 1
        print("now : %d" % count)
        next_url = "https://m.place.naver.com/restaurant/%s/menu/list" % i
        driver.get(next_url)
        time.sleep(0.5)
        driver.implicitly_wait(0)
        if len(driver.find_elements(By.CLASS_NAME, "naver_order_contents")) == 0:
            driver.implicitly_wait(1)
            res = crawl_without_naver_order(driver, i)
            if res != None:
                fin.append(res)
        else:
            driver.implicitly_wait(1)
            fin.append(crawl_with_naver_order(driver, i))


fin = []
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# time.sleep(5)
# saveUniqueNumber()
