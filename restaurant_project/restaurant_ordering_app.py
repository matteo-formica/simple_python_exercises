class Order:
    def __init__(self,customer_name, customer_id, dishes=[], price=0.0, completed="False"):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.dishes = dishes
        self.price = round(float(price), 2)
        self.completed = completed
        

class Customer:
    def __init__(self, name, address, id, past_orders=[], favourite_dishes=[]):
        self.name = name
        self.address = address
        self.id = id
        self.past_orders = past_orders
        self.favourite_dishes = favourite_dishes

    def retrieve_favourite(self):
        favourite ={}

    
class Restaurant:
    def __init__(self, name, address, passwd, menu={}, customers=[], orders=[], totalincome = 0.0, totalorders=0):
        self.name = name
        self.address = address
        self.menu = menu
        self.customers = customers
        self.orders = orders
        self.passwd = passwd
        self.totalincome = totalincome
        self.totalorders = totalorders
    
    def initialize(self):
        self.menu = {}
        self.customers = []
        self.orders = []
        self.totalincome = 0
        with open("restaurant_project/restaurant.txt", 'r') as f:
            for line in f.readlines():
                income, ordernum = line.split(',')
                self.totalincome = float(income)
                self.totalorders = int(ordernum.strip('\n'))
        with open("restaurant_project/menu.txt") as f:
            for line in f.readlines():
                string = line
                key, value = string.split(",")                   
                self.menu[key] = float(value)
        with open("restaurant_project/customers.txt") as f:
            for line in f.readlines():
                string = line
                name, address, id = string.split(',')
                customer = Customer(name, address, int(id))
                self.customers.append(customer)
        with open("restaurant_project/orders.txt") as f:
            self.totalorders = 0
            self.totalincome = 0.0
            for line in f.readlines():
                self.totalorders += 1
                string = line
                name, id, price, dishes, completed = string.split(',')
                dish = list(dishes.split(';'))
                order = Order(name, int(id), dish, float(price), completed.strip("\n"))
                self.orders.append(order)
                self.totalincome += float(price)
                with open("restaurant_project/restaurant.txt", 'w') as f:
                    f.write(str(self.totalincome) + ',' + str(self.totalorders) + '\n')
            
    def add_dish(self):
        key = input("What's the dish's name? ").strip().title()
        value = str(round(float(input("What's the dish's price? ").strip()), 2))
        with open("restaurant_project/menu.txt", 'a') as f:
            f.write(key + "," + value + "\n")
        self.initialize()

    def add_customer(self):
        name = input("Customer's name: ").strip().title()
        address = input("Customer's address: ").strip().title()
        id = int(len(self.customers) + 1)
        with open("restaurant_project/customers.txt", 'a') as f:
            f.write(name + ',' + address + ',' + str(id) + "\n")
        self.initialize()

    def take_order(self, idn):
        id = idn
        for customer in self.customers:
            if id != customer.id:
                continue
            else:
                order = Order(customer.name, customer.id)
                order.dishes = []
        completed = False
        while not completed:
            dish = input("choose a dish: ").title()
            for key in self.menu.keys():
                if dish != key:
                    continue
                else:
                    order.dishes.append(key)
                    order.price += self.menu[key]
            goon = input("Do you want to add anything?(y/n) ").strip().lower()
            if goon != "y":
                print(f"Order review: Customer ID: {order.customer_id} Total price: ${order.price}")
                confirm = input("Do you confirm your order?(y/n): ").strip().lower()
                if confirm != "y":
                    continue
                else:
                    self.totalincome += order.price
                    with open("restaurant_project/restaurant.txt", 'w') as f:
                        f.write(str(self.totalincome))
                    with open("restaurant_project/orders.txt", 'a') as f:
                        f.write(order.customer_name + ',' + str(order.customer_id) + ',' + str(order.price) + ',' + ";".join(order.dishes) + ',' + order.completed + '\n')
                    for customer in self.customers:
                        if id == customer.id:
                            customer.past_orders.append(order)
                    print("Order submitted successfully!")
                    completed = "True"
                    self.initialize()

    def update_order(self):
        with open("restaurant_project/orders.txt", 'w') as f:
            for order in self.orders:
                f.write(order.customer_name + ',' + str(order.customer_id) + ',' + str(order.price) + ',' + ";".join(order.dishes) + ',' + order.completed + '\n')
        self.initialize()

    def manage_orders(self):
        if len(self.orders) == 0:
            print("There are no orders here!")
            q = input("Press any key to return to menu")
        else:
            for order in self.orders:
                i = 1
                if order.completed != "True":
                    print(f"Orders n°{i} of ID n°{order.customer_id}, Customer name: {order.customer_name}")
                    for dish in order.dishes:
                        print(f"1x {dish}")
                    print(f"Total order's price: {order.price}")
                    completed = input("Do you want to set this order as completed?(y/n) ").strip().lower()
                    if completed == "y":
                        print(f"Order n°{i} completed!")
                        order.completed = "True"
                        self.update_order()
                i += 1
            print("You've reached the end of order's list")
            q = input("Press any key to return to menu")

restaurant = Restaurant("Bully", "Via Ciccia 63", "1234")


def restaurant_side(passwd):
    while True:
        if passwd != restaurant.passwd:
            print("Wrong Password! Try again..")
        else:
            print("------------------------------")
            print()
            print("1. Reastaurant information")
            print("2. Customer list")
            print("3. Add Customer")
            print("4. Add Dish")
            print("5. Manage orders")
            print("6. Return to side selection")
            print()
            print("------------------------------")
            select = int(input("Choose an option: ").strip())
            if select not in [1, 2, 3, 4, 5, 6]:
                print("Invalid selection")
                continue
            match select:
                case 1:
                    print(f"Restaurant name: {restaurant.name}")
                    print(f"Restaurant address: {restaurant.address}")
                    print(f"Statistics: Total income: ${restaurant.totalincome} | Total orders : {restaurant.totalorders}")
                    q = input("Press any key to return to menu")
                case 2:
                    for customer in restaurant.customers:
                        print(f"ID: {customer.id} | Name: {customer.name} | Address: {customer.address} | Past orders: {len(customer.past_orders)}")
                    q = input("Press any key to return to menu")
                case 3:
                    restaurant.add_customer()
                case 4:
                    restaurant.add_dish()
                case 5:
                    restaurant.manage_orders()
                case 6:
                    break


def customer_side(id):
    while True:
        print("------------------------------")
        print()
        print("1. Customer information")
        print("2. Restaurant's menu")
        print("3. Order")
        print("4. Return to side selection")
        print()
        print("------------------------------")
        select = int(input("Choose an option: ").strip())
        if select not in [1, 2, 3, 4]:
            print("Invalid selection")
            continue
        match select:
            case 1:
                for customer in restaurant.customers:
                    if id != customer.id:
                        continue
                    else:
                        print(f"Customer ID: {customer.id}")
                        print(f"Customer name: {customer.name}")
                        print(f"Restaurant address: {customer.address}")
                        print(f"Favourite dish: --")
                        print(f"Past orders: {len(customer.past_orders)}")
                q = input("Press any key to return to menu")
            case 2:
                for dish, price in restaurant.menu.items():
                    print(f"- {dish}: ${price}")
                q = input("Press any key to return to menu")
            case 3:
                restaurant.take_order(id)
            case 4:
                break


def side_selection():
    while True:
        print("------------------------------")
        print()
        print("1. Reastaurant dashboard")
        print("2. Customer Dashboard")
        print("3. Quit")
        print()
        print("------------------------------")
        select = int(input("Choose an option: ").strip())
        if select not in [1, 2, 3]:
            print("Invalid selection")
            continue
        elif select == 1:
            passwd = input("Password: ")
            restaurant_side(passwd)
        elif select == 2:
            id = int(input("Write your customer ID: ").strip())
            customer_side(id)
        else:
            print("Thank you! See you soon")
            break


def main():
    restaurant.initialize()
    side_selection()


main()