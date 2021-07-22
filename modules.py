#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

from os import remove

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

    return urls
