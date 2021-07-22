#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from selenium import webdriver
import modules

x = 0

driver_path = "/usr/bin/chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--lang = fr")
option.add_argument("--headless")

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option, )

browser.get("https://www.oiseaux.net/oiseaux/france.html")

cookies = browser.find_element_by_id("cookie_cancel")
cookies.click()

birds_list = browser.find_elements_by_xpath('//*[@id="oiseaux"]/div/div/div[1]/div[2]/table/tbody/tr/td[5]/a')

modules.url_recovering(birds_list)
urls = modules.url_sorting()

for i in urls:
    browser.get(i)
    modules.information_file_and_image(browser, i)