class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = id(product_id)
        self.name = name
        self.price = price
        self.stock = stock
