menu_items = ['Latte', 'Cappuccino', 'Espresso', 'Mocha', 'Americano', 'Macchiato', 'Affogato', 'Croissant', 'Danish', 'Cherry pie', 'Glazed donut', 'Long John', 'Water', 'Tea', 'Refresher']
menu_items_lower = [item.lower() for item in menu_items] 

def print_menu():
    print()
    for items in menu_items:
        print(items)
    print()

def order_again():
    while True:
            print("\nWould you like to order anything else or is that all for you?")
            order_again = input("If you would like to order again type '1'. If that is all type 'X': ")

            if order_again == "1":
                print()
                print_menu()
                order_again = input("What else would you like to order?: ")

            if order_again.lower() == "x":
                break
            else:
                continue
    print("\nThank you! have a nice day 🙂")

print("\n----------------------------------")
print("\n☕️ Welcome to Boulangerie Cafe! ☕️\n")
print("----------------------------------\n")


input1 = input("Would you like to take a look at our menu? [type yes or no]: ")
print()

while input1.lower() not in ["yes", "no"]:
    input1 = input("Invalid input. Please type 'yes' or 'no': ")

if input1.lower() == "no":
   no_input = input("What would you like to order?: ")

   if no_input.lower() in menu_items_lower:
       print(f"You would like to order {no_input.capitalize()}.")

       order_again()
    
   while no_input not in menu_items_lower:
        print((f"\nCurrently we do not sellf {no_input.capitalize()} or it is sold out.\n"))
        print_menu()
        no_input = input("Please choose from this menu: ")
        
        if no_input.lower() in menu_items_lower:
            print(f"You would like to order {no_input.capitalize()}.")
            order_again()

if input1.lower() == "yes":
    print("\nPlease take your time to look!")
    print_menu()
    input2 = input("What would you like to order?: ")

    if input2.lower() in menu_items_lower:
        print(f"\nYou would like to order {input2.capitalize()}.")

        order_again()

    while input2.lower() not in menu_items_lower:
        print((f"\nCurrently we do not sellf {input2.capitalize()} or it is sold out.\n"))
        print_menu()
        input2 = input("Please choose from this menu: ")
        
        if input2 in menu_items_lower:
            print(f"You would like to order {input2.capitalize()}.")
            order_again()