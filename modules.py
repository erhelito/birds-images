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

def url_sorting() :
    j = ""
    useless_url = "https://www.oiseaux.net/oiseaux/\n"
    sorted_urls = []

    file = open("url_list.txt", "r")
    urls = file.readlines()
    file.close()
    remove("url_list.txt")

    for i in urls :
        if i == useless_url :
            urls.remove(i)

        elif i == j:
            urls.remove(i)

        j = i

    for i in urls :
        sorted_urls.append(i[0:-1])

    return sorted_urls

def information_file_and_image(browser, article_url) :
    name = browser.find_element_by_class_name("titre")
    name = name.text

    print(name)

    order = browser.find_element_by_class_name("order")
    order = order.text

    description = browser.find_element_by_xpath('//*[@id="description-esp"]/div/p')
    description = description.text

    data = browser.find_elements_by_class_name("on_bio_titre")
    data = data[2]
    data = data.text

    image_url = browser.find_element_by_class_name("on_img_id")
    image_url = image_url.get_attribute("src")
    image_url = get(image_url)

    if path.exists(order) is False :
        mkdir(order)

    image = open(f"{order}/{name}.png", "wb")
    image.write(image_url.content)
    image.close()

    description_file = open(f"{order}/{name}.txt", "w")
    description_file.write(
        f"""Nom : {name}
Ordre : {order}

{data}

Description : {description}

URL de l'article pour plus d'informations : {article_url}"""
    )

    print("Done")