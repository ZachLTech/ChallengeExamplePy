# Initialize the player's inventory and game state
inventory = []
found_map = False

# Define the game loop
while True:
    print("\nYou are Alden, a blacksmith's apprentice on a quest to find the Lost Kingdom of Eldoria.")
    print("You stand at a crossroads in the Forbidden Forest. What do you do?\n")
    print("1. Take the left path.")
    print("2. Take the right path.")
    print("3. Check your inventory.")
    print("4. Quit the game.")
    
    # Get the player's choice
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\nYou venture down the left path and encounter a friendly traveler.")
        print("They offer you an old map that might lead to Eldoria's lost kingdom.")
        print("What do you do?")
        print("1. Accept the map.")
        print("2. Decline and continue on your own.")
        
        inner_choice = input("Enter your choice: ")
        
        if inner_choice == '1':
            print("\nYou accept the map and thank the traveler. It's added to your inventory.")
            inventory.append("Eldoria Map")
            found_map = True
        elif inner_choice == '2':
            print("\nYou decline the map and bid farewell to the traveler. You continue your journey.")
        else:
            print("\nInvalid choice. Please try again.")
    
    elif choice == '2':
        if found_map:
            print("\nWith the map in hand, you confidently take the right path.")
            print("You stumble upon a hidden cave entrance.")
            print("What do you do?")
            print("1. Enter the cave.")
            print("2. Turn back and explore elsewhere.")
            
            inner_choice = input("Enter your choice: ")
            
            if inner_choice == '1':
                print("\nYou bravely enter the cave, ready to face whatever lies within.")
                print("\n\nTo be continued... (probably not)")
                break
            elif inner_choice == '2':
                print("\nYou decide it's too dangerous and turn back, seeking another path.")
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("\nYou hesitate to take the right path without a map. Perhaps you should find one first.")
    
    elif choice == '3':
        print("\nInventory:")
        for item in inventory:
            print(item)
    
    elif choice == '4':
        print("\nYou have chosen to quit the game. Thanks for playing!")
        break
    
    else:
        print("\nInvalid choice. Please try again.")

