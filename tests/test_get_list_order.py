import allure
import requests

from curl import GET_LIST_ORDERS

@allure.feature("Получение списка заказов")
class TestGetListOrders:

    @allure.title("Получение списка заказов возвращает список")
    def test_get_list_of_orders(self):
        response = requests.get(GET_LIST_ORDERS)

        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
