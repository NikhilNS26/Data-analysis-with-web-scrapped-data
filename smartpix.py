from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/asus/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.smartprix.com/mobiles")

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(3)

old_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        break
    old_height = new_height


html_source = driver.page_source
with open("smartprix.html", "w", encoding="utf-8") as f:
    f.write(html_source)