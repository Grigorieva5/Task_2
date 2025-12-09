import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.user_methods import UserMethods
import allure
from data import *


class TestCreateOrder:

    @allure.title('Создание заказа без авторизации')
    def test_create_order_not_auth_user(self, clean_order):
        order_data, status_code = clean_order(params=ORDER_DATA, token=None)

        assert (status_code == 200 and
                order_data["success"] == True and
                "name" in order_data and
                "order" in order_data and
                "number" in order_data["order"])
        

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_auth_user(self, clean_order):
        user_data, _ = UserMethods().post_login_user(params=LOGIN_USER)
        token = user_data['accessToken']
        order_data, status_code = clean_order(params=ORDER_DATA,token=token)

        assert (status_code == 200 and
                order_data["success"] == True and
                "name" in order_data and
                "order" in order_data and
                "price" in order_data["order"] and
                "ingredients" in order_data["order"])
        

    @allure.title('Создание заказа без ингредиентов')
    @pytest.mark.parametrize('token', [None, "get_token"])
    def test_create_order_without_ingredients(self, token, clean_order):
        ingredient = []
        if token == "get_token":
            user_data, _ = UserMethods().post_login_user(params=LOGIN_USER)
            token = user_data['accessToken']

        order_data, status_code = clean_order(params=ingredient,token=token)

        assert (status_code == 400 and
            order_data == {
                "success": False,
                "message": "Ingredient ids must be provided"
            })
        
    @allure.title('Создание заказа с неверным хешем ингредиентов под неавторизованным пользователем')
    @pytest.mark.parametrize('invalid_data', ORDER_INVALID_DATA)
    def test_create_order_invalid_ingredients_not_auth(self, invalid_data, clean_order):
   
        order_data, status_code = clean_order(params=invalid_data,token=None)

        assert (status_code == 500 and 
                "<pre>Internal Server Error</pre>" in order_data and
                "<html" in order_data and
                "Internal Server Error" in order_data)

    @allure.title('Создание заказа с неверным хешем ингредиентов под авторизованным пользователем')
    @pytest.mark.parametrize('invalid_data', ORDER_INVALID_DATA)
    def test_create_order_invalid_ingredients_auth(self, invalid_data, clean_order):
        user_data, _ = UserMethods().post_login_user(params=LOGIN_USER)
        token = user_data['accessToken']
        order_data, status_code = clean_order(params=invalid_data,token=token)

        assert (status_code == 500 and 
                "<pre>Internal Server Error</pre>" in order_data and
                "<html" in order_data and
                "Internal Server Error" in order_data)    