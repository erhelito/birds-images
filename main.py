#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from selenium import webdriver
import requests
from os import mkdir, path, system
import modules

x = 0

driver_path = "/usr/bin/chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--headless")

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://www.oiseaux.net/oiseaux/france.html")

cookies = browser.find_element_by_id("cookie_cancel")
cookies.click()

birds_list = browser.find_elements_by_xpath('//*[@id="oiseaux"]/div/div/div[1]/div[2]/table/tbody/tr/td/a')

modules.url_recovering(birds_list)
urls = modules.url_sorting()

for i in range(len(birds_list)) :
    print("{0}/{1}".format(i+1, len(birds_list)))

    birds_list_in_loop = browser.find_elements_by_xpath('//*[@id="oiseaux"]/div/div/div[1]/div[2]/table/tbody/tr/td/a')

    birds_list_in_loop[x].click()

    bird_name = browser.find_element_by_class_name("titre")
    bird_name = bird_name.text

    print(bird_name)

    order = browser.find_element_by_class_name("order")
    order = order.text

    main_image = browser.find_element_by_class_name("on_img_id")
    image_url = main_image.get_attribute("src")

    image_file = requests.get(image_url)

    if path.isdir(order) is False :
        mkdir(path = "{0}".format(order))

    file = open("{0}/{1}.png".format(order, bird_name), "wb")
    file.write(image_file.content)
    file.close()

    print("Done")

    browser.get("https://www.oiseaux.net/oiseaux/france.html")

    system("clear")

    x+=1