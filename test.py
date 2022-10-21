from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

path = "C:\Program Files (x86)\chromedriver.exe"
url = 'https://www.glassdoor.ca/Job/data-scientist-jobs-SRCH_KO0,14.htm'

driver = webdriver.Chrome(executable_path=path)
driver.set_window_size(1120, 1000)
driver.get(url)


for i in range(1, 15):
    job = driver.find_element_by_xpath("//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]").click()
    time.sleep(2)
    company = driver.find_element_by_xpath("//*[@id='JDCol']/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]").text
    title = driver.find_element_by_xpath("//*[@id='JDCol']/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]").text
    location = driver.find_element_by_xpath("//*[@id='JDCol']/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]").text

    print(company, title, location)


    try:
        close = driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span').click() #clicking to the X.
        print(' x out worked')
    except NoSuchElementException:
        pass
    time.sleep(3)
