def display_menu():
    print("Welcome to Cozy Coffee Corner! ☕")
    print("\nMenu:")
    print("1. Coffee")
    print("2. Sandwich")
    print("3. Pastry")

def get_coffee_order():
    price = 3  # Base price for coffee
    size = input("Choose size (Small - $3, Medium - $4, Large - $5): ").strip().lower()
    if size == "medium":
        price += 1
    elif size == "large":
        price += 2
    
    extra_shot = input("Do you want an extra espresso shot? (+$1) (yes/no): ").strip().lower()
    if extra_shot == "yes":
        price += 1
    
    return price

def get_sandwich_order():
    price = 5  # Base price for sandwich
    filling = input("Choose filling (Veg - $5, Chicken - $6, Beef - $7): ").strip().lower()
    if filling == "chicken":
        price += 1
    elif filling == "beef":
        price += 2
    
    meal = input("Do you want to make it a meal? (yes/no): ").strip().lower()
    if meal == "yes":
        drink = input("Choose a drink (Water - $2, Juice - $5): ").strip().lower()
        if drink == "water":
            price += 2
        elif drink == "juice":
            price += 5
    
    return price

def get_pastry_order():
    price = 4  # Base price for pastry
    type_pastry = input("Choose type (Regular - $4, Sugarless - $5, Eggless - $5): ").strip().lower()
    if type_pastry in ["sugarless", "eggless"]:
        price += 1
    
    return price

def main():
    display_menu()
    choice = input("Please select an item (1-3): ").strip()
    total_price = 0
    
    if choice == "1":
        total_price = get_coffee_order()
    elif choice == "2":
        total_price = get_sandwich_order()
    elif choice == "3":
        total_price = get_pastry_order()
    else:
        print("Invalid selection! Exiting...")
        return
    
    dine_option = input("Do you want takeaway or dine-in? ").strip().lower()
    print(f"\nThank you for your order! Your total is: ${total_price}")
    print("Have a great day! ☕")

if __name__ == "__main__":
    main()
