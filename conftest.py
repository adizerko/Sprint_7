import pytest
import requests

from curl import CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER, CANCEL_ORDER, CREATE_ORDER, GET_ORDER_BY_TRACK
from data import Payloads
from generation import Generation
from helper import register_new_courier_and_return_login_password


@pytest.fixture
def login_courier():
    login, password, first_name = register_new_courier_and_return_login_password()
    login_courier_body = {"login": login, "password": password}
    response = requests.post(LOGIN_COURIER, json=login_courier_body)

    yield response

    requests.delete(f"{DELETE_COURIER}/{response.json()['id']}")
    assert response.status_code == 200


@pytest.fixture()
def create_courier():
    login = Generation.login()
    password = Generation.password()
    first_name = Generation.first_name()

    create_courier_body = {"login": login, "password" :password, "firstName": first_name}
    login_courier_body = {"login": login, "password" :password}

    requests.post(CREATE_COURIER, json=create_courier_body)
    payload = {
        "login": login,
        "password": password
    }

    yield payload
    login_courier = requests.post(LOGIN_COURIER, json=login_courier_body)
    response_del = requests.delete(f'{DELETE_COURIER}{login_courier.json()["id"]}')
    assert response_del.status_code == 200


@pytest.fixture
def delete_courier():
    def delete(login, password):
        response = requests.post(LOGIN_COURIER, json={"login":login, "password": password})
        if response.status_code == 200:
            response_delete = requests.delete(f"{DELETE_COURIER}/{response.json()['id']}")
            assert response_delete.status_code == 200

    yield delete


@pytest.fixture
def canceled_order():
    def cancel(track):
        response = requests.put(CANCEL_ORDER, json=track)
        assert response.status_code == 200

    yield cancel


@pytest.fixture
def create_order_and_get_id(create_order):
    track_id = create_order
    params = {"t": track_id}
    order_id = requests.get(GET_ORDER_BY_TRACK, params=params).json()["order"]["id"]

    return order_id


@pytest.fixture
def create_order():
    response = requests.post(CREATE_ORDER, json=Payloads.full_order_black_and_grey)
    track_id = response.json()["track"]

    return track_id
