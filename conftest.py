import pytest
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from data import *


@pytest.fixture
def clean_order():
    created_orders = []
    
    def _create_order(params, token=None):
        order_methods = OrderMethods()
        order_data, status_code = order_methods.post_orders(params=params, token=token)
        
        created_orders.append((order_data, token))
        
        return order_data, status_code 
    
    yield _create_order 
    
    # Автоматически удаляем все созданные заказы
    for order_data, token in created_orders:
        if ("order" in order_data and "number" in order_data["order"]):
            order_id = order_data["order"]["number"]
            try:
                OrderMethods().delete_order(order_id, token)
            except:
                pass

@pytest.fixture
def create_user():
    user_data, status_code = UserMethods().post_create_user()
    
    yield user_data, status_code

    UserMethods().delete_user(token=user_data['accessToken'])            