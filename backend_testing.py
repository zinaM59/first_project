import requests  # HTTP library for get/ post


url = "http://127.0.0.1:5000"  # api endpoint'
user_id = 20
user_name = "example"
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

