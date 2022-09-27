from selenium import webdriver as driver


PATH = "C:\Program Files (x86)\chromedriver.exe"    # Path to open in windows

driver = driver.Chrome(PATH)                        # If using windows use this driver
#driver = driver.Chrome()                           # If using mac use this driver even though it isnt fully automated yet
driver.get('https://www.google.ca/')

print('driver')
