import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
import allure
from data import *


class TestGetOrders:

    @allure.title('Получение заказов без авторизации')
    def test_get_orders_not_auth_user(self):
        order_data, status_code = OrderMethods().get_orders_user(token=None)

        assert (status_code == 401 and
                order_data == {
                    "success": False,
                    "message": "You should be authorised"
                })
        

    @allure.title('Получение заказов с авторизацией')
    def test_get_orders_auth_user(self):
        user_data, _ = UserMethods().post_login_user(params=LOGIN_USER)
        token = user_data['accessToken']
        order_data, status_code = OrderMethods().get_orders_user(token=token)

        assert (status_code == 200 and
                order_data["success"] == True and
                "orders" in order_data and
                "total" in order_data and
                "totalToday" in order_data and
                order_data["orders"][0]["status"] == "done" and
                "price"  not in order_data["orders"][0] and
                "ingredients" in order_data["orders"][0])   
        