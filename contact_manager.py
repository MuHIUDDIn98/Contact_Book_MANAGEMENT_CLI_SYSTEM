from contact import Contact
import file_handler

class ContactManager:
    def __init__(self):
        self.contacts = file_handler.load_contacts()

    def add_contact(self, name, phone, email, address):
        if any(c.phone == phone for c in self.contacts):
            return False, "Phone number already exists."
        try:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            file_handler.save_contacts(self.contacts)
            return True, "Contact added successfully."
        except ValueError as e:
            return False, str(e)

    def view_contacts(self):
        return self.contacts

    def search_contact(self, term):
        return [c for c in self.contacts if term.lower() in c.name.lower()
                or term in c.phone or term.lower() in c.email.lower()]

    def remove_contact(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                self.contacts.remove(c)
                file_handler.save_contacts(self.contacts)
                return True, "Contact deleted."
        return False, "Contact not found."