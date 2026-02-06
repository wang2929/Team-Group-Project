# create dict for contacts
contacts = {
   "Bob": {
        "name" : "Bob",
        "lastname": "",
        "phone": "777-888-9999",
     
        }
}


def manage_contacts():
    print("Welcome to the contact manager!! \n 1. Create contact \n 2. Search contact \n 3. Update contact \n 4. Delete contact ")
    option = input("Please choose a number (1-4)")
    def http_status_code(status):
        match option:
            case "1":
                 create_contact()
            case "2":
                 search_contact()
            case "3":
                 update_contact()
            case "4":
                 delete_contact()

# create function
def create_contact():
    name = input("Please enter name: ")
    phone = input("Please enter phone number: ")
    contacts["name"] = name
    contacts["phone"] = phone
    return contacts

# update function
def update_contact():
    name_to_search = input("Please enter contact name to update: " )
    for contact in contacts:
        if name_to_search == contacts[contact]:
            print(contacts["name"])
    


# delete function
def delete_contact():
    pass

# search function
def search_contact():
    pass
    
print(update_contact())
