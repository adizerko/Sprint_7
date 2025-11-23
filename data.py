from generation import Generation


class Payloads:
    minimal = {
        "login": Generation.login(),
        "password": Generation.password()
    }

    full = {
        "login": Generation.login(),
        "password": Generation.password(),
        "firstName": Generation.first_name()
    }

    missing_login = {"password": Generation.password(), "firstName": Generation.first_name()}
    missing_password = {"login": Generation.login(), "firstName": Generation.first_name()}
    missing_firstName = {"login": Generation.login(), "password": Generation.password()}
    login_missing = {"password": Generation.password()}
    password_missing = {"login": Generation.login()}
    invalid_login = {"login": Generation.login(), "password": Generation.password()}


    full_order_random_color = {
        "firstName": Generation.first_name(),
        "lastName": Generation.last_name(),
        "address": Generation.address(),
        "metroStation": Generation.metro(),
        "phone": Generation.phone(),
        "rentTime": Generation.rent_time(),
        "deliveryDate": Generation.delivery_date(),
        "comment": Generation.comment(),
        "color": [Generation.color()
    ]
}

    full_order_black_and_grey = {
        "firstName": Generation.first_name(),
        "lastName": Generation.last_name(),
        "address": Generation.address(),
        "metroStation": Generation.metro(),
        "phone": Generation.phone(),
        "rentTime": Generation.rent_time(),
        "deliveryDate": Generation.delivery_date(),
        "comment": Generation.comment(),
        "color": ["BLACK", "GREY"]
}

    full_order_no_color = {
        "firstName": Generation.first_name(),
        "lastName": Generation.last_name(),
        "address": Generation.address(),
        "metroStation": Generation.metro(),
        "phone": Generation.phone(),
        "rentTime": Generation.rent_time(),
        "deliveryDate": Generation.delivery_date(),
        "comment": Generation.comment(),
        "color": []
    }


class ExpectedResponses:
    SUCCESS = { "ok": True }
    INSUFFICIENT_DATA = {"message": "Недостаточно данных для создания учетной записи"}
    DUPLICATE_COURIER = {"message": "Этот логин уже используется"}
    ACCOUNT_NOT_FOUND = {"message": "Учетная запись не найдена"}
    INSUFFICIENT_LOGIN_DATA = {"message":  "Недостаточно данных для входа"}
    INSUFFICIENT_DELETE_DATA = {"message":  "Недостаточно данных для удаления курьера"}
    COURIER_NOT_FOUND = {"message": "Курьера с таким id нет"}
    INSUFFICIENT_DATA_FOR_SEARCH = {"message": "Недостаточно данных для поиска"}
    COURIER_ID_NOT_FOUND = {"message": "Курьера с таким id не существует"}
    ORDER_ID_NOT_FOUND = {"message": "Заказа с таким id не существует"}
    ORDER_NOT_FOUND = {"message": "Заказ не найден"}
