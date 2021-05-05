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
        return r.status_code

    def get_user_data(self):
        r = requests.get("http://127.0.0.1:5000/user/api")


print(TestingJWT("Benharushtomer@gmail.com", "aaaaa").get_token())
