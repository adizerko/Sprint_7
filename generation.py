import random
from datetime import datetime
from random import randint

from faker import Faker


faker = Faker("ru_RU")

class Generation:

    @staticmethod
    def login():
        return faker.user_name()

    @staticmethod
    def password():
        return faker.password()

    @staticmethod
    def first_name():
        return faker.first_name()

    @staticmethod
    def last_name():
        return faker.last_name()

    @staticmethod
    def address():
        return faker.street_name()

    @staticmethod
    def metro():
        return randint(1, 200)

    @staticmethod
    def phone():
        return randint(100000000000,  9999999999999)

    @staticmethod
    def rent_time():
        return randint(1,7)

    @staticmethod
    def delivery_date():
        return datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def color():
        color = ["BLACK", "GREY"]
        return random.choice(color)

    @staticmethod
    def comment():
        return faker.text(50)
