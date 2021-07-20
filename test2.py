from selenium import webdriver
import time, requests

driver_path = "/usr/bin/chromedriver"
brave_path = "/usr/bin/brave-browser"

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

def search_google(search_query):
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # open browser and begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')

    count = 0
    for e in elements:
        # get images source url
        e.click()
        time.sleep(1)
        element = browser.find_elements_by_class_name('v4dQwb')

        # Google image web site logic
        if count == 0:
            big_img = element[0].find_element_by_class_name('n3VNCb')
        else:
           big_img = element[1].find_element_by_class_name('n3VNCb')

        images_url.append(big_img.get_attribute("src"))

        # write image to file
        reponse = requests.get(images_url[count])
        if reponse.status_code == 200:
            with open(f"search{count+1}.jpg","wb") as file:
                file.write(reponse.content)

        count += 1

        # Stop get and save after 5
        if count == 5:
            break

    return images_url

items = search_google('dog')