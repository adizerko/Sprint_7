from random import randint

import allure
import requests

from curl import GET_ORDER_BY_TRACK
from data import ExpectedResponses

@allure.feature("Получение заказа по номеру")
class TestGetOrderByNumber:
    def test_get_order_by_track_success(self, create_order):
        track_id = create_order
        params = {"t": track_id}
        response = requests.get(GET_ORDER_BY_TRACK, params=params)

        assert response.status_code == 200
        assert isinstance(response.json()["order"], dict)

    @allure.title("Ошибка при получении заказа без номера")
    def test_get_order_by_track_without_number_returns_error(self, create_order):
        params = {"t": ""}
        response = requests.get(GET_ORDER_BY_TRACK, params=params)

        assert response.status_code == 400
        assert response.json() == ExpectedResponses.INSUFFICIENT_DATA_FOR_SEARCH

    @allure.title("Ошибка при получении заказа с несуществующим номером")
    def test_get_order_by_track_nonexistent_number_returns_error(self):
        params = {"t": randint(1000000, 9999999)}
        response = requests.get(GET_ORDER_BY_TRACK, params=params)

        assert response.status_code == 404
        assert response.json() == ExpectedResponses.ORDER_NOT_FOUND
