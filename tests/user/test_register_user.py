import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.user_methods import UserMethods
import allure
from data import *


class TestRegisterUser:

    @allure.title('Успешная регистрация пользователя')
    def test_register_user_success(self):
        user_data, status_code = UserMethods().post_create_user()

        assert (status_code == 200 and
                user_data["success"] == True and
                "user" in user_data and
                "email" in user_data["user"] and
                "name" in user_data["user"] and
                "accessToken" in user_data and
                "refreshToken" in user_data)
        
        delete_result, delete_status = UserMethods().delete_user(token=user_data['accessToken']) 
        assert delete_status == 202 and delete_result["success"] == True
    
        
    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_register_dublicate_user(self):
        user_data, status_code = UserMethods().post_create_user(REGISTER_USER)

        assert (status_code == 403 and
                user_data == {
                        "success": False,
                        "message": "User already exists"
                    }
                )

    @allure.title('Регистрация пользователя без обязательного поля')
    @pytest.mark.parametrize("invalid_data", REGISTER_INVALID_DATA)
    def  test_register_user_without_mandatory_field(self, invalid_data):
        user_data, status_code = UserMethods().post_create_user(params=invalid_data)
        assert (status_code == 403 and
                user_data == {
                    "success": False,
                    "message": "Email, password and name are required fields"
                }
                )
          
