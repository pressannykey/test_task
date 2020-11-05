import allure
from framework import check
from framework.jsonplaceholder_client import Client
import pytest


@allure.suite("GET /posts")
class TestGetPosts:
    @allure.title("Positive. Get all posts")
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check.check_get_all_posts_response(response)

    @pytest.mark.parametrize("userid", [1, 10])
    @allure.title("Positive. Get posts by userId {userid}")
    def test_get_posts_by_existing_user(self, userid):
        response = Client().get_posts_by_userid(userid)
        check.check_response_field(response, "userId", userid)
        check.check_get_posts_by_userid(response, 10)

    @allure.title("Negative. Get posts by userId 0")
    def test_get_posts_by_user(self):
        response = Client().get_posts_by_userid(0)
        check.check_get_posts_by_userid(response, 0)

    @pytest.mark.parametrize("post_id", [1, 100])
    @allure.title("Positive. Get post by id {post_id}")
    def test_get_existing_post(self, post_id):
        response = Client().get_post_by_id(post_id)
        check.check_response_code(response, 200)

    @pytest.mark.parametrize("post_id", [0, 101])
    @allure.title("Negative. Get post by id {post_id}")
    def test_get_post(self, post_id):
        response = Client().get_post_by_id(post_id)
        check.check_response_code(response, 404)
