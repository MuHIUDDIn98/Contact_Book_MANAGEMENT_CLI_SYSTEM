class Contact:
    def __init__(self, name, phone, email, address):
        if not name.replace(" ", "").isalpha() or len(name.strip()) < 2:
            raise ValueError("Name must only contain letters and spaces (min 2 characters).")

        if not phone.startswith("+880") or not phone[4:].isdigit() or len(phone) != 14:
            raise ValueError("Phone number must be in the format +880XXXXXXXXXX (11 digits after +880).")

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Invalid email format.")

        self.name = name.strip()
        self.phone = phone
        self.email = email.strip()
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["name"], data["phone"], data["email"], data["address"])