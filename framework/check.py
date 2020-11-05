import allure
from hamcrest import assert_that, equal_to
from requests import codes
from framework.utils import data_validation, field_validation


def _response_general_check(response, expected_code=codes.ok):
    assert_that(
        response.status_code,
        equal_to(expected_code),
        f"Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}",
    )


@allure.step
def check_response_code(response, expected_code):
    return _response_general_check(response, expected_code=expected_code)


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(
        len(response.json()),
        equal_to(100),
        f"Expected post count: 100. Actual count {len(response.json())}",
    )


@allure.step
def check_get_posts_by_userid(response, count):
    _response_general_check(response)
    assert_that(
        len(response.json()),
        equal_to(count),
        f"Expected post count: {count}. Actual count {len(response.json())}",
    )


@allure.step
def check_response_field(response, field, reference):
    assert_that(
        field_validation(response, field, reference),
        f"Response value should be equal to the sent value",
    )


@allure.step
def check_response_data(response, data):
    assert_that(
        data_validation(response, data),
        "Response should contains all fields of the sent data",
    )
