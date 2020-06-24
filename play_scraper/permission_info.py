from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from unidecode import unidecode
import time

chrome_driver_path = '/Users/grtushar/Documents/libs/chromedriver'
options = Options()
options.headless = True
driver = webdriver.Chrome(chrome_driver_path, options=options)


def get_permission_info(soup2):
    ret = ""

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
