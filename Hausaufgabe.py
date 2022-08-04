# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver")

liste = ['Nürnberg','Frankfurt','Heppenheim','Fürth']

driver.get("https://www.google.de")

time.sleep(4)
alle_ablehnen = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]/div")
alle_ablehnen.click()

time.sleep(4)
search_bar = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_bar.send_keys(liste[0])
eingabetaste = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
eingabetaste.click()


title = driver.find_element(by=By.CLASS_NAME, value="yuRUbf")
#Title_Link = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[10]/div[1]/div[1]/div[3]/div/div[1]/div/div/div/div[1]')
print(title.text)
entfernt = liste.pop(0)

for x in liste :
    time.sleep(4)
    search_bar = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    search_bar.send_keys(Keys.CONTROL+"a")
    search_bar.send_keys(Keys.BACK_SPACE)
    search_bar.send_keys(x)

    eingabetaste2 = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    eingabetaste2.send_keys(Keys.ENTER)


    title = driver.find_element(by=By.CLASS_NAME, value="yuRUbf")
    print(title.text)
    




