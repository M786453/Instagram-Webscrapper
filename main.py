import time

import openpyxl

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


wb = openpyxl.load_workbook("followers.xlsx")

sheets = wb.sheetnames

sheet_followers_dict = {}

for sheet in sheets:
    followers = []

    followers_col = wb[sheet]['A']

    for follower in followers_col:
        if str(type(follower.value)) != "<class 'NoneType'>":
            followers.append(follower.value)

    sheet_followers_dict.update({sheet: followers})

#
# options = Options()
# options.headless = True     # with this option, we will scrap in background
# driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe", options=options)

driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")

driver.get("https://www.instagram.com/home/")

for sheet in sheet_followers_dict:

    followers = sheet_followers_dict[sheet]

    if len(followers) > 0:

        for f in range(0, len(followers)):

            search = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

            search.clear()

            search.send_keys(followers[f])

            time.sleep(5)

            search.send_keys(Keys.ENTER)

            time.sleep(5)

            search.send_keys(Keys.ENTER)

            try:
                time.sleep(5)
                driver.find_element_by_class_name("rkEop")
                wb[sheet]["B" + str(f + 1)] = "Account is Private"  # writing account status in excel file
                print(followers[f] + "'s Account is Private")
            except NoSuchElementException:
                wb[sheet]["B" + str(f + 1)] = "Account is Public"
                print(followers[f] + "'s Account is Public")

wb.save("New.xlsx")
