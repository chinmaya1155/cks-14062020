from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
username_displayed = driver.find_element_by_id("txtUsername")
username_enabled = driver.find_element_by_id("txtUsername")
print("The user name field displayed: " + str(username_displayed.is_displayed()))
print("The user name field enabled: " + str(username_enabled.is_enabled()))
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
driver.find_element_by_xpath("//*[@id='menu_time_viewTimeModule']/b").click()
driver.find_element_by_name("time[startingDays]").send_keys("Monday")
#driver.close()
print("Test complete")

