from data import load_data, save_data
from product_model import Product
from customer_model import Customer
from orders_model import Orders

class DataManager:
    def __init__(self):
        self._products = None
        self._customers = None
        self._orders = None

    def _load_if_needed(self):
        if self._products is None or self._customers is None or self._orders is None:
            self._products, self._customers, self._orders = load_data()

    def _save(self):
        save_data(self._products, self._customers, self._orders)

    def get_all_products(self):
        self._load_if_needed()
        return self._products

    def add_product(self, name, price, stock):
        self._load_if_needed()
        new_id = max([p.id for p in self._products], default=0) + 1
        new_product = Product(new_id, name, price, stock)
        self._products.append(new_product)
        self._save()
        return new_product

    def update_product(self, product_id, name, price, stock):
        self._load_if_needed()
        for product in self._products:
            if product.id == product_id:
                product.name = name
                product.price = price
                product.stock = stock
                self._save()
                return True
        return False

    def delete_product(self, product_id):
        self._load_if_needed()
        for product in self._products:
            if product.id == product_id:
                self._products.remove(product)
                self._save()
                return True
        return False

    def get_customer_by_email(self, email):
        self._load_if_needed()
        return next((c for c in self._customers if c.email == email), None)

    def add_customer(self, name, email):
        self._load_if_needed()
        if any(c.email == email for c in self._customers):
            return None
        new_id = max([c.id for c in self._customers], default=0) + 1
        new_customer = Customer(new_id, name, email)
        self._customers.append(new_customer)
        self._save()
        return new_customer

    def place_order(self, customer_id, product_id, quantity):
        self._load_if_needed()
        product = next((p for p in self._products if p.id == product_id), None)
        if product and product.stock >= quantity:
            order_id = max([o.id for o in self._orders], default=0) + 1
            order = Orders(order_id, customer_id, product_id, quantity)
            self._orders.append(order)
            product.stock -= quantity
            self._save()
            return order
        return None

    def get_orders_by_customer(self, customer_id):
        self._load_if_needed()
        return [o for o in self._orders if o.customer_id == customer_id]
