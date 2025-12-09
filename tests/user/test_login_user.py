import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.user_methods import UserMethods
import allure
from data import *


class TestLoginrUser:

    @allure.title('Успешная авторизация пользователя')
    def test_login_user_success(self):
        user_data, status_code = UserMethods().post_login_user(params=LOGIN_USER)

        assert (status_code == 200 and
                user_data["success"] == True and
                "user" in user_data and
                "email" in user_data["user"] and
                "name" in user_data["user"] and
                "accessToken" in user_data and
                "refreshToken" in user_data)
      
    @allure.title('Аторизация с неверным логином и паролем')
    @pytest.mark.parametrize("invalid_data", LOGIN_INVALID_DATA)
    def  test_login_user_false(self, invalid_data):
        user_data, status_code = UserMethods().post_login_user(params=invalid_data)
        
        assert (status_code == 401 and
                user_data == {
                    "success": False,
                    "message": "email or password are incorrect"
                }
                )    