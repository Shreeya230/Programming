#question 1
items = ['sql', '123', 'python']
result = list(filter(lambda x: x.isalpha(), items))
print(result)

#question 2 
products = [
    {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
    {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}
]
instock_products = list(filter(lambda p: p['instock'] == True, products))
print(instock_products)

#question 3 
def calculate_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total
print(calculate_sum(1, 5))

#question 4 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! cannot divide by zero"
    return a / b

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            print("Exiting calculator")
            break
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        else:
            print("Invalid choice")
calculator()

#question 5
course = [
    {'title': 'Ancient Civilizations', 'genre': 'history'},
    {'title': 'Corporate Finance', 'genre': 'commerce'},
    {'title': 'Modern World History', 'genre': 'history'}
]
history_course = list(filter(lambda h: h['genre'] == 'history', course))
print(history_course)

#question 6
emails = [
    'user@gmail.com',
    'offer@spam.com',
    'admin@company.com',
]

blacklist = ['spam.com']

spam_emails = list(filter(
    lambda email: email.split('@')[1] in blacklist,
    emails
))
print(spam_emails)

#question 7
price = [100, 50, 200, 75]
discounted_price = list(map(lambda p: p * 0.8, price))
print(discounted_price) 

#question 8
def skip_two(lst):
    return [lst[i] for i in range(1, min(len(lst), 12), 3)]
print(skip_two([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))

#question 9 
def remove_at_idx(lst, idx):
    if idx < 0 or idx >= len(lst):
        return lst
    return lst[:idx] + lst[idx + 1:]
print(remove_at_idx([10, 20, 30, 40, 50], 2))

#question 10 
user_input = input("Enter a string: ")
cleaned_string = ''.join(
    map(lambda c: c if c.isalnum() else '#', user_input)
)
print("Cleaned string:", cleaned_string)

#question 11
# Global dictionary to store users
users_db = {}

def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username] = {
        "password": password,
        "email": email
    }
    return f"Registration successful for {username}"

def login_user(username, password):
    if username not in users_db:
        return "User not found"
    if users_db[username]["password"] != password:
        return "Incorrect password"
    return f"Welcome back, {username}"

# Testing with given users
print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))

print(login_user("ram", "ram123"))
print(login_user("hari", "wrongpass"))
print(login_user("gita", "123"))

#question 12 
inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]

def add_product(name, price, quantity):
    for item in inventory:
        if item['name'].lower() == name.lower():
            print("Product already exists")
            return
    if price <= 0 or quantity <= 0:
        print("Price and quantity must be positive")
        return
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print("Product added successfully")

def view_products():
    print("\nName\tPrice\tQuantity")
    for item in inventory:
        print(f"{item['name']}\t{item['price']}\t{item['quantity']}")

def update_product(name):
    for item in inventory:
        if item['name'].lower() == name.lower():
            item['price'] = int(input("Enter new price: "))
            item['quantity'] = int(input("Enter new quantity: "))
            print("Product updated successfully")
            return
    print("Product not found")

def delete_product(name):
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            print("Product deleted successfully")
            return
    print("Product not found")

def total_inventory_value():
    total = sum(item['price'] * item['quantity'] for item in inventory)
    print("Total inventory value:", total)

while True:
    print("\n1.Add  2.View  3.Update  4.Delete  5.Total Value  6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product(
            input("Name: "),
            int(input("Price: ")),
            int(input("Quantity: "))
        )
    elif choice == 2:
        view_products()
    elif choice == 3:
        update_product(input("Enter product name: "))
    elif choice == 4:
        delete_product(input("Enter product name: "))
    elif choice == 5:
        total_inventory_value()
    elif choice == 6:
        print("Exiting inventory system")
        break
    else:
        print("Invalid choice")

#question 13
contacts = [
    {'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}
]

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def valid_email(email):
    return '@' in email and '.' in email

def add_contact(name, phone, email):
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact already exists")
            return
    if not valid_phone(phone):
        print("Invalid phone number")
        return
    if not valid_email(email):
        print("Invalid email format")
        return
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print("Contact added successfully")

def display_contacts():
    for c in contacts:
        print(c)

def search_contact(name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            print(c)
            return
    print("Contact not found")

def update_contact(name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            print("Contact updated")
            return
    print("Contact not found")

def delete_contact(name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted")
            return
    print("Contact not found")

def sort_contacts():
    contacts.sort(key=lambda x: x['name'].lower())
    print("Contacts sorted alphabetically")

while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Sort 7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_contact(
            input("Name: "),
            input("Phone: "),
            input("Email: ")
        )
    elif ch == 2:
        display_contacts()
    elif ch == 3:
        search_contact(input("Enter name: "))
    elif ch == 4:
        update_contact(input("Enter name: "))
    elif ch == 5:
        delete_contact(input("Enter name: "))
    elif ch == 6:
        sort_contacts()
    elif ch == 7:
        print("Exiting contact manager")
        break
    else:
        print("Invalid choice")

