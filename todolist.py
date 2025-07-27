# to do list

    


to_do = [ ]

while True:
    print("This is your to do list so far: ")
    for item in to_do:
        print("□", item)
    print("\nWhat would you like to do?")
    answer = input("1. Add to list,\n2. Mark item as done \n3. Delete \n4. Exit (type Q to quit) \nPlease enter a choice: ")

    if answer == "1":
        task = input("\nEnter task: ")
        to_do.append(task)
        print()
        print(", ".join(to_do))
        print()

    elif answer == "2":
        done = input("\nWhich item would you like to mark as done?: ")
        if done not in to_do:
            print(f"\n{done.capitalize()} is not found in the list\n")
            continue
        index = to_do.index(done)
        to_do[index] += "✅"
        print("Task marked as done!")
    
    elif answer == "3":
        delete = input("Which item would you like to delete?: ")
        if delete in to_do:
            to_do.remove(delete)
        if delete not in to_do:
            print(f"\n{delete.capitalize()} not found in list.\n")

    elif answer == "Q" or answer == "q": 
        break

    else:
        print("\nPlease enter a valid option\n")

print("\nSee you again soon!")