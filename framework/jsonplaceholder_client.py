import allure
import requests as r
import json
from config import JSONPLACEHOLDER_HOST


class Client:
    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, data):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=data)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f"/posts")

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f"/posts/{post_id}")

    @allure.step
    def create_new_post_from_file(self, file):
        with open(file, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
            return self._post(path=f"/posts", data=data)

    @allure.step
    def create_new_post(self, data):
        return self._post(path=f"/posts", data=data)

    @allure.step
    def get_posts_by_userid(self, user_id: int):
        return self._get(path=f"/posts?userId={user_id}")
