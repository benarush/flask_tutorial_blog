import requests
import json


class TestingJWT:

    def __init__(self, username="test", password="test"):
        self.username = username
        self.password = password

    def get_token(self):
        data = {
                "username": self.username,
                "password": self.password
        }
        r = requests.post("http://127.0.0.1:5000/token", data=data)
        self.token = None if r.status_code != 200 else json.loads(r.text).get("access_token")
        print(self.token)
        return r.status_code

    def get_user_data(self):
        r = requests.get("http://127.0.0.1:5000/user/api",
                         headers={'Authorization': 'Bearer ' + self.token})
        return r.status_code

    def get_posts(self):
        r = requests.get("http://127.0.0.1:5000/posts/api",
                         headers={'Authorization': 'Bearer ' + self.token})
        return r.status_code

#jwt = TestingJWT("Benharushtomer@gmail.com", "aaaaa")
#print(jwt.get_token())
# print(jwt.get_posts())
# print(jwt.get_user_data())
