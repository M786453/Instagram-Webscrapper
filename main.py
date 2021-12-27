import time

import openpyxl

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

wb = openpyxl.load_workbook("E:/InstaScrapProject/followers.xlsx")

sheets = wb.sheetnames

followers = []

followers_col = wb['pesaschile']['A']

for f in followers_col:
    followers.append(f.value)

driver = webdriver.Chrome("C:/Users/Ahtesham Sarwar/Downloads/chromedriver_win32/chromedriver.exe")

# driver.get("https://www.instagram.com/")




# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
#
# username.clear()
# password.clear()
#
# username.send_keys("USERNAME-HERE")
#
# password.send_keys("PASSWORD-HERE")
#
# logIn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"Log In")]'))).click()
#
# not_now_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()
#
# not_now_btn2 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Not Now")]'))).click()

driver.get("https://www.instagram.com/home/")

for s in range(0, len(followers)):

    search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))

    search.clear()

    search.send_keys(followers[s])

    time.sleep(5)

    search.send_keys(Keys.ENTER)

    time.sleep(5)

    search.send_keys(Keys.ENTER)

    try:
        time.sleep(5)
        driver.find_element_by_class_name("rkEop")
        wb['pesaschile']["B" + str(s+1)] = "Account is Private"  # writing account status in excel file
        print(followers[s] + "'s Account is Private")
    except NoSuchElementException:
        wb['pesaschile']["B" + str(s+1)] = "Account is Public"
        print(followers[s] + "'s Account is Public")

wb.save("New.xlsx")
