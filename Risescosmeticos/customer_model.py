class Customer:
    def __init__(self, customer_id, name: str, email: str):
        self.id = id(customer_id)
        self.name = name
        self.email = email