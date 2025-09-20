from random import randint

import allure
import requests

from curl import DELETE_COURIER
from data import ExpectedResponses


@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_successful(self, login_courier):
        response_login = login_courier
        response_delete = requests.delete(
            f"{DELETE_COURIER}/{response_login.json()['id']}"
        )

        assert response_delete.status_code == 200
        assert response_delete.json() == ExpectedResponses.SUCCESS

    @allure.title("Ошибка при удалении курьера без указания id")
    def test_delete_courier_without_id_returns_error(self, login_courier):
        response_delete = requests.delete(f"{DELETE_COURIER}")

        assert response_delete.status_code == 400
        assert response_delete.json() == ExpectedResponses.INSUFFICIENT_DELETE_DATA

    @allure.title("Ошибка при удалении курьера с несуществующим id")
    def test_delete_courier_nonexistent_id_returns_error(self):
        response_delete = requests.delete(
            f"{DELETE_COURIER}/{randint(999999, 99999999)}"
        )

        assert response_delete.status_code == 404
        assert response_delete.json() == ExpectedResponses.COURIER_NOT_FOUND
