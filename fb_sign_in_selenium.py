from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##Launch Facebook
driver = webdriver.Chrome("C:\\Users\\v-brfon\\Desktop\\chromedriver.exe")
driver.get('http://www.facebook.com')

##credential asks
name = str(input('Please input email or phone number: '))
password = str(input('Please input your password: '))

driver.find_element_by_id('email').send_keys(name)
print('typing user...')
driver.find_element_by_id('pass').send_keys(password)
print('typing pass...')

driver.find_element_by_id('u_0_2').click()

print('User input sign in')
