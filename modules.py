#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from os import remove, path, mkdir, listdir
from requests import get
from shutil import copyfile

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

def find_name(browser) :
    try :
        name = browser.find_element_by_class_name("titre")
        name = name.text

        return name
    except :
        print("Can't find the name")

def find_order(browser) :
    try :
        order = browser.find_element_by_class_name("order")
        order = order.text

        return order
    except :
        print("Can't find the order")

def find_description(browser) :
    try :
        description = browser.find_element_by_xpath('//*[@id="description-esp"]/div/p')
        description = description.text

        return description
    except :
        print("Can't find the description")

def find_data(browser) :
    try :
        data = browser.find_elements_by_class_name("on_bio_titre")
        data = data[2]
        data = data.text

        return data
    except :
        print("Can't find the data")

def create_directory_if_necessary(order) :
    if path.exists(order) is False :
        mkdir(order)

def create_description_file(name, order, data, description, article_url) :
    description_file = open(f"{order}/{name}.txt", "w")
    description_file.write(
        f"""Nom : {name}
Ordre : {order}

{data}

Description : {description}

URL de l'article pour plus d'informations : {article_url}"""
)

def create_image_file(browser, order, name) :
    try:
        image_url = browser.find_element_by_class_name("on_img_id")
        image_url = image_url.get_attribute("src")
        image_url = get(image_url)

        with open(f"{order}/{name}.jpeg", "wb") as image:
            image.write(image_url.content)
    except :
        print("Can't find an image")

def fetch_orders() :
    files = listdir()
    orders_list = []

    for i in files :
        file = "." not in i

        if file :
            orders_list.append(i)

    return orders_list

def create_images_for_orders(orders_list):
    for i in orders_list:

        x = 0

        files_in_folder = listdir(i)

        try :
            while (files_in_folder[x])[-5:] != ".jpeg" :
                x += 1
            
            copyfile(f"{i}/{files_in_folder[x]}", f"{i}.jpeg")

        except :
            ""