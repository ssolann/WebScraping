from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path, slp_time):


    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = 'https://www.glassdoor.ca/Job/'+keyword+'-jobs-SRCH_KO0,14.htm'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:
        for i in range(1, num_jobs):

            job = driver.find_element_by_xpath("//*[@id='MainCol']/div[1]/ul/li["+str(i)+"]").click()
            collected_successfully = False

            while not collected_successfully:
                try:
                    company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text()
                    job_title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text()
                    location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text()

                    print(company_name, job_title, location)
                except:
                    time.sleep(2)


                try:
                    close = driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span').click() #clicking to the X.
                    print(' x out worked')
                except NoSuchElementException:
                    pass
                time.sleep(3)
