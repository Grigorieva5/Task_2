import requests
from data import *
import json
import allure


class OrderMethods:

    @allure.title('Создание заказа')
    def post_orders(self, params, token=None):
        # сделано так для универсальности метода (работает и с токеном, и без)
        headers = {}
        if token:
            headers['Authorization'] = token
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json = params, headers=headers)
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code
        

    @allure.step('Удаление заказа')
    def delete_order(self, order_id, token=None):
        # сделано так для универсальности метода (работает и с токеном, и без)
        headers = {}
        if token:
            headers['Authorization'] = token
        try:
            response = requests.delete(f'{BASE_URL}{DELETE_URL}/{order_id}', headers=headers)
            try:
                return response.json(), response.status_code
            except json.JSONDecodeError:
                return response.text, response.status_code 
        except:
            return "Не удалось удалить заказ", 500
          
    @allure.step('Получение заказов конкретного пользователя')
    def get_orders_user(self, token):
        response = requests.get(f'{BASE_URL}{ORDER_URL}', headers={'Authorization': token})
        
        try:
            return response.json(), response.status_code    
        except json.decoder.JSONDecodeError:
            return response.text, response.status_code        