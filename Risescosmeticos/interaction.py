from product_model import Product
from customer_model import Customer     
from orders_model import Orders
from data import load_data, save_data

class Interaction:
    def __init__(self):
        self.products, self.customers, self.orders = load_data()

    def start(self):
        print("Welcome to the Product Management System!")
        while True:
            print("1. View Manager")
            print("2. View Customer")
            print("3. Exit")
            choice = input("Please select an option: ")
            if choice == '1':
                self.view_manager()
            elif choice == '2':
                self.view_customer()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_manager(self):
        print("Manager View")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        choice = input("Please select an option: ")
        if choice == '1':
            self.view_products()
        elif choice == '2':
            self.add_product()
        elif choice == '3':
            self.update_product()
        elif choice == '4':
            self.delete_product()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please try again.")

    def view_products(self):
        print("Product List:")
        for product in self.products:
            print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock}")

    def add_product(self):
        product_id = int(input("Enter product ID: "))
        if any(p.id == product_id for p in self.products):
            print("Product ID already exists.")
            return
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        new_product = Product(product_id, name, price, stock)
        self.products.append(new_product)
        save_data(self.products, self.customers, self.orders)
        print("Product added successfully.")

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        for product in self.products:
            if product.id == product_id:
                product.name = input("Enter new product name: ")
                product.price = float(input("Enter new product price: "))
                product.stock = int(input("Enter new product stock: "))
                save_data(self.products, self.customers, self.orders)
                print("Product updated successfully.")
                return
        print("Product not found.")

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: "))
        for product in self.products:
            if product.id == product_id:
                self.products.remove(product)
                save_data(self.products, self.customers, self.orders)
                print("Product deleted successfully.")
                return
        print("Product not found.")

    def view_customer(self):
        print("Customer View")
        print("1. Log in")
        print("2. Sign up")
        choice = input("Please select an option: ")
        if choice == '1':
            self.login_customer()
        elif choice == '2':
            self.signup_customer()
        else:
            print("Invalid choice. Please try again.")

    def login_customer(self):
        email = input("Enter your email: ")
        for customer in self.customers:
            if customer.email == email:
                print(f"Welcome back, {customer.name}!")
                self.customer_menu(customer)
                return
        print("Customer not found. Please sign up.")

    def signup_customer(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        if any(c.email == email for c in self.customers):
            print("Email already registered.")
            return
        customer_id = max([c.id for c in self.customers], default=0) + 1
        new_customer = Customer(customer_id, name, email)
        self.customers.append(new_customer)
        save_data(self.products, self.customers, self.orders)
        print("Customer signed up successfully. You can now log in.")

    def customer_menu(self, customer):
        print(f"Welcome, {customer.name}!")
        while True:
            print("1. View Products")
            print("2. Place Order")
            print("3. View Orders")
            print("4. Back to Main Menu")
            choice = input("Please select an option: ")
            if choice == '1':
                self.view_products()
            elif choice == '2':
                self.place_order(customer)
            elif choice == '3':
                self.view_orders(customer)
            elif choice == '4':
                return
            else:
                print("Invalid choice. Please try again.")

    def place_order(self, customer):
        self.view_products()
        product_id = int(input("Enter product ID to order: "))
        for product in self.products:
            if product.id == product_id:
                quantity = int(input("Enter quantity: "))
                if quantity <= product.stock:
                    order_id = max([o.id for o in self.orders], default=0) + 1
                    order = Orders(order_id, customer.id, product.id, quantity)
                    self.orders.append(order)
                    product.stock -= quantity
                    save_data(self.products, self.customers, self.orders)
                    print("Order placed successfully.")
                else:
                    print("Insufficient stock.")
                return
        print("Product not found.")

    def view_orders(self, customer):
        print(f"Orders for {customer.name}:")
        customer_orders = [order for order in self.orders if order.customer_id == customer.id]
        if not customer_orders:
            print("No orders found.")
        else:
            for order in customer_orders:
                product = next((p for p in self.products if p.id == order.product_id), None)
                product_name = product.name if product else "Unknown Product"
                print(f"Order ID: {order.id}, Product: {product_name}, Quantity: {order.quantity}")

