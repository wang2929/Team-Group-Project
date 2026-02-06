# will need functions (def) for the three choices of manage contacts(#2), internet search(#3), and manage tasks(#4)


# main menu 
def main():
    # keep the welcome outside of the loop - it only prints ONCE
    print("Welcome to the Main Menu!\n")
    
# Francisco said use a while loop for the main menu:
    while True:
        # print stuff to choose from
        print ("1. Main Menu")
        print ("2. Manage Contacts")
        print ("3. Internet Search")
        print ("4. Manage Tasks")
        print ("5. Exit")
    
    # call read-from-terminal
        user_choice = input("\nEnter selection: ")
    
    # validation check (is this an option?)
        if user_choice not in ["1", "2", "3", "4", "5"]:
            print("You're wrong - go back and try again lol")
            continue
        # already there
        if user_choice == "1":
            print("You are already in the Main Menu BOZO")
        # manage contacts
        elif user_choice == "2":
            print("You have chosen to Manage Contacts.")
        # internet search
        elif user_choice == "3":
            print("You have chosen Internet Search.")
        # manage tasks
        elif user_choice == "4":
            print("You have chosen Manage Tasks.")
        # code for exiting
        elif user_choice == "5":    
            print("Exiting...")
            break
        else:
            print("Invalid selection....BOZO")