from data_manager import DataManager

class Interaction:
    def __init__(self):
        self.manager = DataManager()

    def start(self):
        print("Welcome to the Product Management System!")
        while True:
            print("\n1. View Manager")
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
        while True:
            print("\nManager View")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                for p in self.manager.get_all_products():
                    print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Stock: {p.stock}")
            elif choice == '2':
                name = input("Enter name: ")
                price = float(input("Enter price: "))
                stock = int(input("Enter stock: "))
                self.manager.add_product(name, price, stock)
                print("Product added.")
            elif choice == '3':
                id = int(input("Enter product ID: "))
                name = input("Enter new name: ")
                price = float(input("Enter new price: "))
                stock = int(input("Enter new stock: "))
                if self.manager.update_product(id, name, price, stock):
                    print("Product updated.")
                else:
                    print("Product not found.")
            elif choice == '4':
                id = int(input("Enter product ID to delete: "))
                if self.manager.delete_product(id):
                    print("Deleted.")
                else:
                    print("Product not found.")
            elif choice == '5':
                break
            else:
                print("Invalid option.")

    def view_customer(self):
        print("\nCustomer View")
        print("1. Log in")
        print("2. Sign up")
        choice = input("Please select an option: ")
        if choice == '1':
            self.login_customer()
        elif choice == '2':
            self.signup_customer()

    def login_customer(self):
        email = input("Enter your email: ")
        customer = self.manager.get_customer_by_email(email)
        if customer:
            print(f"Welcome back, {customer.name}!")
            self.customer_menu(customer)
        else:
            print("Customer not found.")

    def signup_customer(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        customer = self.manager.add_customer(name, email)
        if customer:
            print("Signup successful. You can now log in.")
        else:
            print("Email already registered.")

    def customer_menu(self, customer):
        while True:
            print("\nCustomer Menu")
            print("1. View Products")
            print("2. Place Order")
            print("3. View My Orders")
            print("4. Back to Main Menu")
            choice = input("Choose: ")

            if choice == '1':
                for p in self.manager.get_all_products():
                    print(f"ID: {p.id}, Name: {p.name}, Price: {p.price}, Stock: {p.stock}")
            elif choice == '2':
                product_id = int(input("Enter product ID: "))
                quantity = int(input("Enter quantity: "))
                order = self.manager.place_order(customer.id, product_id, quantity)
                if order:
                    print("Order placed.")
                else:
                    print("Order failed. Insufficient stock or product not found.")
            elif choice == '3':
                orders = self.manager.get_orders_by_customer(customer.id)
                if not orders:
                    print("No orders found.")
                else:
                    for o in orders:
                        product = next((p for p in self.manager.get_all_products() if p.id == o.product_id), None)
                        pname = product.name if product else "Unknown"
                        print(f"Order ID: {o.id}, Product: {pname}, Qty: {o.quantity}")
            elif choice == '4':
                break
            else:
                print("Invalid option.")
