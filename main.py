from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.finelib.com/cities/abuja/government")
driver.implicitly_wait(3)
classID = driver.find_element(By.CLASS_NAME, "cmpny-lstng-1")
print(classID.text)
