from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from unidecode import unidecode
import time

chrome_driver_path = '/Users/grtushar/Documents/libs/chromedriver'
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_driver_path, options=options)


def get_permission_info(url):
    ret = ""

    driver.get(url)
    time.sleep(5)
    source = driver.page_source
    soup1 = BeautifulSoup(source, "lxml")
    view_details_link = soup1.find('a', {'class': 'hrTbp', 'jsname': 'Hly47e'})
    view_details_link = unidecode(view_details_link.text)
    driver.find_element_by_link_text(view_details_link).click()
    time.sleep(5)
    source2 = driver.page_source
    soup2 = BeautifulSoup(source2, "lxml")

    permission_sub_lists = soup2.find_all('ul', {'class': 'GLaCt'})
    permission_contents = []
    for contents in permission_sub_lists:
        plain_contents = []
        for data in contents.find_all('li'):
            plain_contents.append(data.text)
        permission_contents.append(plain_contents)

    permission_list = soup2.find_all('span', {'class': 'SoU6Qc'})
    for i in range(0, len(permission_list)):
        permission = permission_list[i]
        ret += permission.text + "\n"
        print(permission.text)
        for sublistContent in permission_contents[i]:
            ret += sublistContent + "\n"
            print("-" + sublistContent)

    return ret
