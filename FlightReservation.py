from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/chromedriver.exe")
driver.get("http://www.newtours.demoaut.com/")
username_displayed = driver.find_element_by_name("userName")
username_enabled = driver.find_element_by_name("userName")
print("The user name field displayed: " + str(username_displayed.is_displayed()))
print("The user name field enabled: " + str(username_enabled.is_enabled()))
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
flight_type_selected = driver.find_element_by_css_selector("input[value='roundtrip']")
print("Round trip selected: " + str(flight_type_selected.is_selected()))
#driver.close()
print("Test complete")

