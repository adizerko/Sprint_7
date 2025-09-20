from random import randint

import allure
import requests

from curl import ACCEPT_ORDER
from data import ExpectedResponses


@allure.feature("Принять заказа")
class TestAcceptOrder:


    @allure.title("Успешный приём заказа курьером")
    def test_accept_order_successful(self, login_courier, create_order_and_get_id):
        courier_id = login_courier.json()["id"]
        order_id = create_order_and_get_id
        params = {"courierId": courier_id}

        response = requests.put(f"{ACCEPT_ORDER}{order_id}", params=params)

        assert response.status_code == 200
        assert response.json() == ExpectedResponses.SUCCESS

    @allure.title("Ошибка при приёме заказа без id курьера")
    def test_accept_order_without_courier_id_returns_error(
        self, login_courier, create_order_and_get_id
    ):
        order_id = create_order_and_get_id
        response = requests.put(f"{ACCEPT_ORDER}{order_id}")

        assert response.status_code == 400
        assert response.json() == ExpectedResponses.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Ошибка при приёме заказа с неверным id курьера")
    def test_accept_order_with_invalid_courier_id_returns_error(
        self, create_order_and_get_id
    ):
        courier_id = randint(1000000, 9999999)
        order_id = create_order_and_get_id
        params = {"courierId": courier_id}

        response = requests.put(f"{ACCEPT_ORDER}{order_id}", params=params)

        assert response.status_code == 404
        assert response.json() == ExpectedResponses.COURIER_ID_NOT_FOUND

    @allure.title("Ошибка при приёме заказа без id заказа")
    def test_accept_order_without_order_id_returns_error(self, login_courier):
        courier_id = login_courier.json()["id"]
        params = {"courierId": courier_id}

        response = requests.put(f"{ACCEPT_ORDER}", params=params)

        assert response.status_code == 400
        assert response.json() == ExpectedResponses.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Ошибка при приёме заказа с неверным id заказа")
    def test_accept_order_with_invalid_order_id_returns_error(self, login_courier):
        courier_id = login_courier.json()["id"]
        order_id = randint(1000000, 9999999)
        params = {"courierId": courier_id}

        response = requests.put(f"{ACCEPT_ORDER}{order_id}", params=params)

        assert response.status_code == 404
        assert response.json() == ExpectedResponses.ORDER_ID_NOT_FOUND
