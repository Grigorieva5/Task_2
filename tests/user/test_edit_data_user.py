import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..')) # добавляет корневую директорию проекта в путь Python 
# нужно, чтобы импортировать модули из methods/ и data.py
import pytest
from methods.user_methods import UserMethods
import allure
from data import *


class TestEditDataUser:

    @allure.title('Успешная изменение данных авторизованного пользователя')
    # в параметризации зациклила процесс, чтобы он возвращал данные к исходному состоянию и тесты можно было запускать много раз
    @pytest.mark.parametrize("data, login", [(
        {
            "email": "editdata_1@test.ru",
            "name": "editdata_2"
        }, EDIT_DATA),
        ({
            "email": "editdata@test.ru",
            "name": "editdata"
        }, {
            "email": "editdata_1@test.ru",
            "password": "editdata"
        } ) 
    ])
    def test_edit_data_auth_user(self, data, login):
        user_data, _ = UserMethods().post_login_user(params=login)
        token = user_data['accessToken']

        edit_data, status_code = UserMethods().patch_edit_data_user(params=data, token=token)

        assert (status_code == 200 and
                edit_data["success"] == True and
                "user" in edit_data and
                edit_data["user"]["email"] == data["email"] and
                edit_data["user"]["name"] == data["name"])
        
    @allure.title('Изменение данных пользователя без авторизации')
    def test_edit_data_not_auth_user(self):

        edit_data, status_code = UserMethods().patch_edit_data_user(params=EDIT_DATA, token=None)

        assert (status_code == 401 and
                edit_data == {
                    "success": False,
                    "message": "You should be authorised"
                })
        
