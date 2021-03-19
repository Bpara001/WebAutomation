from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(r"C:\Users\Jesse\Desktop\Python_WebScripts\chromedriver")
driver.get('https://www.youtube.com/')
searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys('jordan MA2')

SearchKey= driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
SearchKey.click()










