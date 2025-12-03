BASE_URL = 'https://stellarburgers.education-services.ru/api/'
REGISTER_URL = 'auth/register/'
LOGIN_URL = 'auth/login/'
DELETE_URL = 'auth/user/'
EDIT_URL = 'auth/user/'
ORDER_URL = 'orders'

REGISTER_USER = {
    "email": "grigorieva@test.ru",
    "password": "grigorieva",
    "name": "grigorieva"
}

REGISTER_INVALID_DATA = [
        {"password": "grigorieva",
        "name": "grigorieva"}, 
        {"email": "grigorieva@test.ru",
        "name": "grigorieva"},
        {"email": "grigorieva@test.ru",
        "password": "grigorieva"}          
    ]

LOGIN_USER = {
    "email": "grigorieva@test.ru",
    "password": "grigorieva"
}

LOGIN_INVALID_DATA = [
        {"email": "",
        "password": "grigorieva"},
        {"email": "grigorieva@test.ru",
        "password": ""},
        {"email": "grigorieva",
        "password": "grigorieva"},
        {"email": "grigorieva@test.ru",
        "password": "grigorieva1234"},
        {"email": "grigorieva1234@test.ru",
        "password": "grigorieva1234"}
    ]   

EDIT_DATA = {
    "email": "editdata@test.ru",
    "password": "editdata"
}

ORDER_DATA = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70"]
}

ORDER_INVALID_DATA = [
    {"ingredients": ["61c0c5a71d1f8bdaaa6d"]},
    {"ingredients": ["61c0c5a71dbdaaa6d", "61c0c5a71d1f8223456", "123456a71d1fbdaaa70"]}
]

