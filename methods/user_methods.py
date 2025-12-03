import requests
import random
import string
from data import *
import json
import allure


class UserMethods:

    def __init__(self):
        self.last_created_user = None  

    @allure.step('Генерация данных для создания пользователя')
    def generate_register_data(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

    
        email = f"testuser_{random.randint(1000, 9999)}@gmail.com"
        password = generate_random_string(10)
        name = generate_random_string(10)

        return {
            "email": email,
            "password": password,
            "name": name
        }
    
    @allure.step('Создание пользователя')
    def post_create_user(self, params = None):
        if params is None:
            params = self.generate_register_data()

        self.last_created_user = params.copy()
        response = requests.post(f'{BASE_URL}{REGISTER_URL}', json = params)

        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
        

    @allure.step('Авторизация пользователя')
    def post_login_user(self, params):
        response = requests.post(f'{BASE_URL}{LOGIN_URL}', json = params)
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code


    @allure.step('Удаление пользователя')
    def delete_user(self, token):
        try:
            response = requests.delete(f'{BASE_URL}{DELETE_URL}', headers={'Authorization': token})
            try:
                return response.json(), response.status_code
            except json.JSONDecodeError:
                return response.text, response.status_code 
        except:
            return "Не удалось удалить пользователя", 500
        

    @allure.step('Изменение данных пользователя')
    def patch_edit_data_user(self, params, token):
        response = requests.patch(f'{BASE_URL}{EDIT_URL}', json = params, headers={'Authorization': token})
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code    
        
      
        



