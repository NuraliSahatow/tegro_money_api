import json
import requests
import hashlib
import hmac
import time

#использовать текущее время в секундах для nonce
nonce = int(time.time())

#Извлечения значений из конфига
with open('config.json') as config_file:
    config = json.load(config_file)
public_key = config("public_key")
sectet_key = config("secret_key")
api_key = config("api_key")
email = config("email")
phone = config("phone")
shop_id = config("shop_id")
def generate_signature(params, api_key):
    body = json.dumps(params)
    sign = hmac.new(api_key.encode(), body.encode(), hashlib.sha256).hexdigest()
    return sign

def make_request(url, params, api_key):
    body = json.dumps(params)
    sign = generate_signature(params, api_key)

    headers = {
        "Authorization": f"Bearer {sign}",
        "Content-Type": "application/json"
    }

    response = requests.post(url=url, headers=headers, params=params)
    return response.json()

# Создание заказа
def create_order():
    url = 'https://tegro.money/api/createOrder/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "currency": "RUB",
        "amount": 100,
        "order_id": "1",
        "payment_system": 1,
        "fields": {
            "email": email,
            "phone": phone
        },
        "receipt": {
            "items": [
                {
                    "name": "test item 1",
                    "count": 1,
                    "price": 600
                },
                {
                    "name": "test item 2",
                    "count": 1,
                    "price": 600
                }
            ]
        }
    }

    response = make_request(url, params, api_key)
    print(response)

# Получение списка магазинов
def list_shops():
    url = "https://tegro.money/api/shops/"

    params = {
        "shop_id": shop_id,
        "nonce": nonce
    }

    response = make_request(url, params, api_key)
    print(response)

# Получение баланса
def get_balance():
    url = "https://tegro.money/api/balance/"

    params = {
        "shop_id": shop_id,
        "nonce": nonce
    }

    response = make_request(url, params, api_key)
    print(response)

# Проверка заказа
def check_order():
    url = 'https://tegro.money/api/order/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "order_id": 755555,
        "payment_id": "test order"
    }

    response = make_request(url, params, api_key)
    print(response)

# Получение информации о заказах
def list_orders():
    url = 'https://tegro.money/api/orders/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "page": 1
    }

    response = make_request(url, params, api_key)
    print(response)

# Создание выплаты
def create_withdrawal():
    url = 'https://tegro.money/api/createWithdrawal/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "currency": "RUB",
        "account": "123",
        "amount": 100,
        "payment_id": 1124235,
        "payment_system": 1
    }

    response = make_request(url, params, api_key)
    print(response)

# Получение списка выплат
def list_withdrawals():
    url = 'https://tegro.money/api/withdrawals/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "page": 1
    }

    response = make_request(url, params, api_key)
    print(response)

# Проверка выплаты
def check_withdrawal():
    url = 'https://tegro.money/api/withdrawal/'

    params = {
        "shop_id": shop_id,
        "nonce": nonce,
        "order_id": 755555,
        "payment_id": "test order"
    }

    response = make_request(url, params, api_key)
    print(response)