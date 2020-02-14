from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# set Chrome webdriver
drv_path = "C:/Users/ijhwa/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(drv_path)
driver.implicitly_wait(3)

category = 'ai_ml'
target_url = 'http://www.dinnopartners.com/category/%s/' % (category)
driver.get(target_url)
# assert "Google" in driver.title

html = driver.page_source
soup = bs(html, 'html.parser')

res = soup.body.find_all('h2', class_='title-post entry-title')

i=1
for n in res :
    print("{:06d}: {}" .format(i, n.get_text().lstrip()))
    i = i+1

# assert "No results found." not in driver.page_source

driver.close()
