from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

CHROME_DRIVER_PATH = '/Users/grtushar/Documents/libs/chromedriver'
TIME_TO_LOAD_DATE_IN_SECOND = 5
TIME_TO_LOAD_MODAL_DATA_IN_SECOND = 5
MAX_ATTEMPT = 100

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)


def get_permission_info(url):
    ret = ""

    attempt = 1
    while True:
        driver.get(url)
        time.sleep(TIME_TO_LOAD_DATE_IN_SECOND)
        driver.find_element_by_link_text("View details").click()
        time.sleep(TIME_TO_LOAD_MODAL_DATA_IN_SECOND)
        soup = BeautifulSoup(driver.page_source, "lxml")

        permission_sub_lists = soup.find_all('ul', {'class': 'GLaCt'})
        permission_contents = []
        for contents in permission_sub_lists:
            plain_contents = []
            for data in contents.find_all('li'):
                plain_contents.append(data.text)
            permission_contents.append(plain_contents)

        permission_list = soup.find_all('span', {'class': 'SoU6Qc'})
        for i in range(0, len(permission_list)):
            permission = permission_list[i]
            ret += permission.text + "\n"
            for sublistContent in permission_contents[i]:
                ret += sublistContent + "\n"
        if (len(permission_list) > 0 and len(permission_sub_lists)) or attempt > MAX_ATTEMPT:
            break

        attempt += 1
    return ret
