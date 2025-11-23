import allure
import pytest
import requests

from curl import CREATE_ORDER
from data import Payloads


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с допустимыми цветами")
    @pytest.mark.parametrize(
        "payload",
        [
            Payloads.full_order_random_color,
            Payloads.full_order_black_and_grey,
            Payloads.full_order_no_color,
        ],
    )
    def test_create_order_color_accepts_black_or_grey(self, payload, canceled_order):
        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert isinstance(response.json()["track"], int)
