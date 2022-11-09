from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading

buy_power = {123456789: "buyTime machine", 1000000: "buyPortal", 50000: "buyAlchemy lab", 7000: "buyShipment",
             2000: "buyMine",
             500: "buyFactory",
             100: "buyGrandma", 15: "buyCursor"}

chrome_driver_path = Service("/Users/israelos/Development/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=chrome_driver_path, options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def buy_best_product():
    threading.Timer(5.0, buy_best_product).start()
    money = driver.find_element(By.ID, "money")
    for key, val in buy_power.items():
        if int(money.text.replace(',', '')) >= key:
            product = driver.find_element(By.ID, val)
            product.click()
            break


buy_best_product()

while True:
    cookie.click()
