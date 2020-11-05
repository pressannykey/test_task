import allure
from framework import check
from framework.helper import gen_title, gen_body
from framework.jsonplaceholder_client import Client
import pytest


@allure.suite("POST /posts")
# POST requests have no validation now, tests below are written in case userId and title are required
class TestCreatePosts:
    @pytest.mark.parametrize(
        "data",
        [
            {"title": gen_title(), "body": gen_body(), "userId": "1"},
            {"title": gen_title(), "userId": "10"},
        ],
    )
    @allure.title("Positive. Create new post")
    def test_create_valid_post(self, data):
        response = Client().create_new_post(data)
        check.check_response_code(response, 201)
        check.check_response_data(response, data)

    @pytest.mark.parametrize(
        "data",
        [{"title": gen_title()}, {"userId": 10}, {"random_field": gen_title()}, {}],
    )
    @allure.title("Negative. Create new post")
    def test_create_invalid_post(self, data):
        response = Client().create_new_post(data)
        check.check_response_code(response, 404)
