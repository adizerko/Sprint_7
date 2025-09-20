import allure
import pytest
import requests

from curl import LOGIN_COURIER
from data import Payloads, ExpectedResponses

@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешный вход курьера")
    def test_courier_login_successful(self, create_courier):
        response = requests.post(LOGIN_COURIER, json=create_courier)

        assert response.status_code == 200
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при входе с неверными учетными данными")
    def test_courier_login_with_invalid_credentials(self):
        response = requests.post(LOGIN_COURIER, json=Payloads.invalid_login)

        assert response.status_code == 404
        assert response.json() == ExpectedResponses.ACCOUNT_NOT_FOUND

    @allure.title("Ошибка при входе без обязательных полей")
    @pytest.mark.parametrize(
        "payload",
        [Payloads.login_missing, Payloads.password_missing],
    )
    def test_courier_login_without_required_fields(self, payload):
        response = requests.post(LOGIN_COURIER, json=payload)

        assert response.status_code == 400
        assert response.json() == ExpectedResponses.INSUFFICIENT_LOGIN_DATA
