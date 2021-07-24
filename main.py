#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from selenium import webdriver
import modules

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
    name = modules.find_name(browser)
    print(name)
    order = modules.find_order(browser)
    description = modules.find_description(browser)
    data = modules.find_data(browser)
    modules.create_directory_if_necessary(order)
    modules.create_description_file(name, order, data, description, i)
    modules.create_image_file(browser, order, name)

    print("Done")

orders_list = modules.fetch_orders()
modules.create_images_for_orders(orders_list)