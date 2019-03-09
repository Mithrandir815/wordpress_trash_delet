from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
options = Options()
options.set_headless(True)
driver = webdriver.Chrome(executable_path='chromedriver_path', chrome_options=options)
loginURL = "https://wordpress.com/log-in"
driver.get(loginURL)
time.sleep(3)

username = "user_name" #あなたのユーザー名を入れてください
password = "password" #あなたのパスワードを入れてください

driver.find_element_by_xpath("//input[@name='usernameOrEmail']").send_keys(username)
driver.find_element_by_css_selector("button.button").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_css_selector("button.button").click()
time.sleep(3)


for i in range(40):
    driver.get("wordpress_trash_path")
    time.sleep(3)
    driver.find_element_by_css_selector("button.ellipsis-menu__toggle").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[text()=\"完全に削除する\"]").click();
    time.sleep(1)
    Alert(driver).accept();
    time.sleep(3)
driver.close();
