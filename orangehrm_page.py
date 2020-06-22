from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:/Users/chsah5/PycharmProjects/Drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
driver.close()
print("Test complete")