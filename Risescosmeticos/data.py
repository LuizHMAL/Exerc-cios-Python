import json
from customer_model import Customer
from product_model import Product
from orders_model import Orders

DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)

            products = [
                Product(
                    product_id=prod['id'],
                    name=prod['name'],
                    price=prod['price'],
                    stock=prod['stock']
                ) for prod in data.get('products', [])
            ]

            customers = [
                Customer(
                    customer_id=cust['id'],
                    name=cust['name'],
                    email=cust['email']
                ) for cust in data.get('customers', [])
            ]

            orders = [
                Orders(
                    order_id=ord['id'],
                    customer_id=ord['customer_id'],
                    product_id=ord['product_id'],
                    quantity=ord['quantity']
                ) for ord in data.get('orders', [])
            ]

            return products, customers, orders

    except FileNotFoundError:
        return [], [], []
    except json.JSONDecodeError:
        print("Error decoding JSON from the data file.")
        return [], [], []

def save_data(products, customers, orders):
    data = {
        'products': [
            {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'stock': product.stock
            } for product in products
        ],
        'customers': [
            {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email
            } for customer in customers
        ],
        'orders': [
            {
                'id': order.id,
                'customer_id': order.customer_id,
                'product_id': order.product_id,
                'quantity': order.quantity
            } for order in orders
        ]
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)