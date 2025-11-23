import pytest
import requests
import allure

from curl import CREATE_COURIER
from data import ExpectedResponses, Payloads

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_successful_creation(self, delete_courier):
        payload = Payloads.full
        response = requests.post(CREATE_COURIER, json=payload)

        assert response.status_code == 201
        assert response.json() == ExpectedResponses.SUCCESS

        delete_courier(payload["login"], payload["password"])

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, delete_courier):
        payload = Payloads.full

        response_first_courier = requests.post(CREATE_COURIER, json=payload)
        assert response_first_courier.status_code == 201
        assert response_first_courier.json() == ExpectedResponses.SUCCESS

        response_second_courier = requests.post(CREATE_COURIER, json=payload)
        assert response_second_courier.status_code == 409
        assert response_second_courier.json() == ExpectedResponses.DUPLICATE_COURIER

        delete_courier(payload["login"], payload["password"])

    @allure.title("Нельзя создать курьера без обязательных полей")
    @pytest.mark.parametrize(
        "payload",
        [Payloads.missing_login, Payloads.missing_password],
    )
    def test_cannot_create_courier_without_required_fields(self, payload):
        response = requests.post(CREATE_COURIER, json=payload)

        assert response.status_code == 400
        assert response.json() == ExpectedResponses.INSUFFICIENT_DATA

    @allure.title("Создание курьера только с обязательными полями")
    def test_create_courier_with_required_fields_only(self, delete_courier):
        payload = Payloads.minimal
        response = requests.post(CREATE_COURIER, json=payload)

        assert response.status_code == 201
        assert response.json() == ExpectedResponses.SUCCESS

        delete_courier(payload["login"], payload["password"])
