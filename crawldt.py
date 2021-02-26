from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://translate.google.com/?sl=en&tl=vi&text=scrape%20&op=translate')
sleep(5)
comment_list = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/section/div/div/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]')
print(comment_list.text)