contacts = []
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nAdd Contact")
        store_name = input("Enter Store Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contact = {
            "Store Name": store_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address
        }
        contacts.append(contact)
        print("Contact added successfully!")
    elif choice == "2":
        print("\nContact List")
        if not contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact['Store Name']} - {contact['Phone Number']}")
    elif choice == "3":
        search_term = input("\nEnter name or phone number to search: ")
        found = False
        for contact in contacts:
            if search_term in contact["Store Name"] or search_term in contact["Phone Number"]:
                print(f"\nFound Contact: {contact}")
                found = True
        if not found:
            print("No matching contacts found.")
    elif choice == "4":
        print("\nUpdate Contact")
        search_term = input("Enter name or phone number of the contact to update: ")
        found = False
        for contact in contacts:
            if search_term in contact["Store Name"] or search_term in contact["Phone Number"]:
                print(f"Updating Contact: {contact}")
                contact["Store Name"] = input("Enter new Store Name: ")
                contact["Phone Number"] = input("Enter new Phone Number: ")
                contact["Email"] = input("Enter new Email: ")
                contact["Address"] = input("Enter new Address: ")
                print("Contact updated successfully!")
                found = True
                break
        if not found:
            print("No matching contact found.")
    elif choice == "5":
        print("\nDelete Contact")
        search_term = input("Enter name or phone number of the contact to delete: ")
        found = False
        for contact in contacts:
            if search_term in contact["Store Name"] or search_term in contact["Phone Number"]:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break
        if not found:
            print("No matching contact found.")
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
