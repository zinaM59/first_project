
from selenium import webdriver
from selenium.webdriver.common.by import By
#get driver
driver = webdriver.Chrome(executable_path="D:\\devops\\chromedriver.exe")
#navigate to web page
driver.get("http://127.0.0.1:5001/users/get_user_name/5")
#get element  by it id
element = driver.find_element(By.ID, "user")
#print element content
print(element.get_attribute("innerHTML"))
