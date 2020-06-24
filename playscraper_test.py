from play_scraper import api
import json

details = api.details('com.twentythreeandme.app')
details.pop('description_html', None)
print(json.dumps(details, indent=4))



# options = Options()
# options.headless = True
# driver = webdriver.Chrome('/Users/grtushar/Documents/libs/chromedriver', options=options)
# try:
#     attempt = 1
#     while True:
#         driver.get(details.get("url"))
#         time.sleep(3)
#         source = driver.page_source
#         soup1 = BeautifulSoup(source, "lxml")
#         viewDetailsLink = soup1.find('a', {'class': 'hrTbp', 'jsname': 'Hly47e'})
#         viewDetailsLink = unidecode(viewDetailsLink.text)
#         # print(viewDetailsLink)
#         driver.find_element_by_link_text(viewDetailsLink).click()
#         time.sleep(2)
#         source2 = driver.page_source
#         soup2 = BeautifulSoup(source2, "lxml")
#         # print(source2)
#         # print(soup2.text)
#
#         print("attempt: " + str(attempt))
#         attempt += 1
#         permissionSubLists = soup2.find_all('ul', {'class': 'GLaCt'})
#         permissionContents = []
#         for contents in permissionSubLists:
#             plainContents = []
#             for data in contents.find_all('li'):
#                 plainContents.append(data.text)
#             permissionContents.append(plainContents)
#
#         permissionList = soup2.find_all('span', {'class': 'SoU6Qc'})
#         print()
#         for i in range(0, len(permissionList)):
#             permission = permissionList[i]
#             print(permission.text)
#             for sublistContent in permissionContents[i]:
#                 print("-" + sublistContent)
#
#         if len(permissionList) > 0 and len(permissionSubLists):
#             break
# finally:
#     driver.quit()

# print('hello from link: ', end='')
