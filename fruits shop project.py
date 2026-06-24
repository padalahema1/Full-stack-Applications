# Fruits Shop Billing System with Login

# Login Credentials
USERNAME = "admin"
PASSWORD = "1234"

# Login
print("========== FRUITS SHOP BILLING SYSTEM ==========")
print("\nLogin")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == USERNAME and password == PASSWORD:
    print("\nLogin Successful!")

    # Fruits Shop Billing System

fruits = {
    "Apple": 120,
    "Banana": 40,
    "Orange": 80,
    "Mango": 150,
    "Grapes": 90
}

total_amount = 0

print("===== WELCOME TO FRUITS SHOP =====")

while True:
    print("\nAvailable Fruits:")
    for fruit, price in fruits.items():
        print(f"{fruit} - ₹{price}/kg")

    fruit_name = input("\nEnter fruit name: ").title()

    if fruit_name in fruits:
        quantity = float(input("Enter quantity (kg): "))

        amount = fruits[fruit_name] * quantity
        total_amount += amount

        print(f"{fruit_name} = ₹{amount}")

    else:
        print("Sorry! Fruit not available.")

    choice = input("\nDo you want to buy more fruits? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===== FINAL BILL =====")
print("Total Amount = ₹", total_amount)
print("Thank You! Visit Again.")
