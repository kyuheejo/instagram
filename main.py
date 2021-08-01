from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

ID = 'dai.lyvitamin' #instagram ID
PW = 'coco0408!' #instagram password 

# open browser
browser = webdriver.Chrome('./chromedriver')
browser.get("https://instagram.com")

# wait while loading
time.sleep(2)

# find and enter login ID 
login_id = browser.find_element_by_name('username')
login_id.send_keys(ID)

# find and enter login password 
login_pw = browser.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

time.sleep(5)

# search for tag
search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#맛스타그램')

time.sleep(1)

# press enter twice to move to top result  
search.send_keys(Keys.RETURN) # focus to top result 
search.send_keys(Keys.RETURN) # move to top result in new window

# select top post
time.sleep(10)
feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
feed.send_keys(Keys.ENTER)
