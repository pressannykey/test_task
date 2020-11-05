import allure
from framework import check
from framework.helper import gen_comment_data
from framework.jsonplaceholder_client import Client
import pytest
import random


@pytest.fixture
def valid_data():
    post_id = random.randint(1, 100)
    return gen_comment_data(post_id)


@pytest.fixture
def invalid_data():
    return gen_comment_data(101)


@allure.suite("POST /comments")
# POST requests have no validation now, tests below are written in case postId should exist
class TestCreateComments:
    @allure.title("Positive. Create new comment")
    def test_create_valid_post(self, valid_data):
        response = Client().create_new_comment(valid_data)
        check.check_response_code(response, 201)
        check.check_response_data(response, valid_data)

    @allure.title("Negative. Create new comment")
    def test_create_invalid_post(self, invalid_data):
        response = Client().create_new_comment(invalid_data)
        check.check_response_code(response, 404)
