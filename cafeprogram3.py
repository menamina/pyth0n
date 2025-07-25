# this is my second cafe program this time using append() method

ordered_items= [ ]
menu_items = ['Latte', 'Cappuccino', 'Espresso', 'Mocha', 'Americano', 'Macchiato', 'Affogato', 'Croissant', 'Danish', 'Cherry pie', 'Glazed donut', 'Long John', 'Water', 'Tea', 'Refresher']
menu_items_lower = [item.lower() for item in menu_items] 
again_again = [print(item) for item in ordered_items]

def print_menu():
    print()
    for items in menu_items:
        print(items)
    print()

def order_again():
    while True:
            print_menu()
            order_again = input("What else can I get you? (Q to quit): ")
            ordered_items.append(order_again)
            print(f"Okay! You would like to order {again_again}.")

                

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
   cart = input("What would you like to order?: ")

   while cart not in menu_items_lower:
       print(f"We currently do not sell {cart} or are sold out. Here is the menu!\n")
       print_menu()
       print()
       cart = input("What would you like to order?: ")

   if cart in menu_items_lower:
       ordered_items.append(cart)
       print(f"\nOkay! You said you wanted to order a: {ordered_items}")
       print("Anything else today?")

       order_again()