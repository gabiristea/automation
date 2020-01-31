from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Gabriel is a great Python Developer! How cool is that!')

user_click = chrome_browser.find_element_by_class_name('btn-default')
user_click.click()

# output = chrome_browser.find_element_by_id('display')
# assert 'Gabriel is a great Python Developer! How cool is that!' in output.text

# chrome_browser.close()
