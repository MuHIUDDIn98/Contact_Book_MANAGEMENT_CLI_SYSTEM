from contact_manager import ContactManager
import re

def print_menu():
    print("""
=========== MENU ===========
1. Add Contact
2. View Contacts
3. Search Contact
4. Remove Contact
5. Exit
============================
""")

def main():
    print("Welcome to the Contact Book CLI System!")
    print("Loading contacts from contacts.csv... Done!")

    manager = ContactManager()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number (format +880XXXXXXXXXX): ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            success, message = manager.add_contact(name, phone, email, address)
            print(message)

        elif choice == "2":
            contacts = manager.view_contacts()
            if not contacts:
                print("No contacts found.")
            else:
                print("\n===== All Contacts =====")
                for i, c in enumerate(contacts, 1):
                    print(f"{i}. Name : {c.name}")
                    print(f"   Phone : {c.phone}")
                    print(f"   Email : {c.email}")
                    print(f"   Address: {c.address}\n")

        elif choice == "3":
            term = input("Enter search term (name/email/phone): ")
            results = manager.search_contact(term)
            if results:
                print("\nSearch Result:")
                for c in results:
                    print(f"Name : {c.name}")
                    print(f"Phone : {c.phone}")
                    print(f"Email : {c.email}")
                    print(f"Address: {c.address}\n")
            else:
                print("No contact found.")

        elif choice == "4":
            phone = input("Enter the phone number of the contact to delete (format +880XXXXXXXXXX): ")
            if not re.match(r"^\+880\d{10}$", phone):
                print("Invalid phone number format. Must be in format +880XXXXXXXXXX.")
                continue
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ").lower()
            if confirm == 'y':
                success, message = manager.remove_contact(phone)
                print(message)

        elif choice == "5":
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()