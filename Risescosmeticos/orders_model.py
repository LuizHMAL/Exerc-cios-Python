class Orders:
    def __init__(self, order_id: int, customer_id: int, product_id: int, quantity: int):
        self.id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity