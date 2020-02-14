from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# set Chrome webdriver
path = "C:/Users/ijhwa/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)

url = "https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F"
driver.get(url)
time.sleep(3)
# assert "Google" in driver.title

# login to the web site with id & password
driver.find_element_by_xpath("""//*[@id="id"]""").send_keys("ijhwanny")
driver.find_element_by_xpath("""//*[@id="inputPwd"]""").send_keys("Aks2rnr3088$")
driver.find_element_by_xpath("""//*[@id="loginBtn"]""").click()

cafe_name = 'mindclimbingclub'
board_name = '_memo'

target_url = 'http://m.cafe.daum.net/%s/%s?boardType=' % (cafe_name, board_name)
driver.get(target_url)
time.sleep(3)

input_num = input('Post Number + Enter: ')
num = int(input_num)
target_url = 'http://m.cafe.daum.net/%s/%s/%d' % (cafe_name, board_name, num)
driver.get(target_url)
time.sleep(3)

# hand over html page source to bs4
html = driver.page_source
soup = bs(html, 'html.parser')

content = soup.body.select_one('#slideArticleList > ul > li > div > strong > span')
print(content)








# assert "No results found." not in driver.page_source

driver.close()
