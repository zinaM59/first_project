import requests  # HTTP library for get/ post

url = "http://127.0.0.1:5000"  # api endpoint'
user_id = 24
user_name = "new user"
#post method
res = requests.post('http://127.0.0.1:5000/data/' + str(user_id), json={"user_name": user_name})
if (res.ok):
    print(res.json())
#get method
res = requests.get('http://127.0.0.1:5000/data/' + str(user_id))
if (res.ok):
    for key, value in res.json().items():
        if key == 'user_name' and value == user_name:
            print(value)
            break


from selenium import webdriver
from selenium.webdriver.common.by import By
#get driver
driver = webdriver.Chrome(executable_path="D:\\devops\\chromedriver.exe")
#navigate to web page
driver.get("http://127.0.0.1:5001/users/get_user_name/5")
#get element  by it id
element = driver.find_element(By.ID, "user")
#get element content
value = element.get_attribute("innerHTML")
print(value)
#check of element content
if value != user_name:
    raise Exception("test failed")

