from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.facebook.com/")

user_box = browser.find_element_by_id("email")
user_box.send_keys("rctrigger89@yahoo.com")
password_box = browser.find_element_by_id("pass")
password_box.send_keys("archieabby0306")
password_box.submit()

browser.get("https://www.facebook.com/pg/gleanson/photos/?tab=albums")
