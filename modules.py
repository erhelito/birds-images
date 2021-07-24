#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from os import remove, path, mkdir
from requests import get

def url_recovering(list) :
    url_list = open("url_list.txt", "w")
    url_list.close()
    url_list = open("url_list.txt", "a")

    for i in list :
        i = i.get_attribute("href")
        url_list.write(i)
        url_list.write("\n")

def url_sorting():
    j = ""
    useless_url = "https://www.oiseaux.net/oiseaux/\n"

    with open("url_list.txt", "r") as file:
        urls = file.readlines()

    remove("url_list.txt")

    for i in urls:
        if i in [useless_url, j]:
            urls.remove(i)

        j = i

    return [i[0:-1] for i in urls]

def find_name(browser, url):
    try:
        name = browser.find_element_by_class_name("titre")
        name = name.text

        return name
    except:
        print("Can't find the name")

        with open("errors.txt", "a") as error_logs:
            error_logs.write(f"{url}, name\n")

def find_order(browser, url):
    try:
        order = browser.find_element_by_class_name("order")
        order = order.text

        return order
    except:
        print("Can't find the order")

        with open("errors.txt", "a") as error_logs:
            error_logs.write(f"{url}, order")

def find_description(browser, url):
    try:
        description = browser.find_element_by_xpath('//*[@id="description-esp"]/div/p')
        description = description.text

        return description
    except:
        print("Can't find the description")

        with open("errors.txt", "a") as error_logs:
            error_logs.write(f"{url}, description\n")

def find_data(browser, url):
    try:
        data = browser.find_elements_by_class_name("on_bio_titre")
        data = data[2]
        data = data.text

        return data
    except:
        print("Can't find the data")

        with open("errors.txt", "a") as error_logs:
            error_logs.write(f"{url}, data\n")

def create_directory_if_necessary(order) :
    try :
        if path.exists(order) is False :
            mkdir(order)

    except :
        print("Error while creating the folder\n")

def create_description_file(name, order, data, description, url) :
    try :
        description_file = open(f"{order}/{name}.txt", "w")
        description_file.write(
        f"""Nom : {name}
Ordre : {order}

{data}

Description : {description}

URL de l'article pour plus d'informations : {url}"""
)

    except :
        print("Error while creating the description file")

def create_image_file(browser, order, name, url):
    try :
        image_url = browser.find_element_by_class_name("on_img_id")
        image_url = image_url.get_attribute("src")
        image_url = get(image_url)

        with open(f"{order}/{name}.jpeg", "wb") as image:
            image.write(image_url.content)
            
    except :
        print("Can't find an image")

        with open("errors.txt", "a") as error_logs:
            error_logs.write(f"{url}, image\n")