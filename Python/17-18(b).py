class TelephoneDirectory:
    def __init__(self):
        self.directory = {}

    def add_contact(self, name, number):
        self.directory[name] = number

    def search_contact(self, name):
        if name in self.directory:
            return f"Name: {name}, Number: {self.directory[name]}"
        else:
            return f"Contact '{name}' not found."

    def display_all_contacts(self):
        if self.directory:
            print("Telephone Directory:")
            for name, number in self.directory.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("Telephone Directory is empty.")

# Creating a telephone directory instance
telephone_dir = TelephoneDirectory()

# Adding contacts
telephone_dir.add_contact("Alice", "1234567890")
telephone_dir.add_contact("Bob", "9876543210")
telephone_dir.add_contact("Charlie", "4567890123")
telephone_dir.add_contact("David", "7890123456")
telephone_dir.add_contact("Eve", "6543210987")
telephone_dir.add_contact("Frank", "3210987654")
telephone_dir.add_contact("Grace", "2109876543")
telephone_dir.add_contact("Harry", "5432109876")
telephone_dir.add_contact("Ivy", "8765432109")
telephone_dir.add_contact("Jack", "2345678901")
telephone_dir.add_contact("Kevin", "9012345678")
telephone_dir.add_contact("Lily", "6789012345")
telephone_dir.add_contact("Mike", "4321098765")
telephone_dir.add_contact("Nancy", "7654321098")
telephone_dir.add_contact("Oliver", "1098765432")
telephone_dir.add_contact("Pam", "8765432109")
telephone_dir.add_contact("Quinn", "5678901234")
telephone_dir.add_contact("Rose", "3456789012")
telephone_dir.add_contact("Sam", "9876543210")
telephone_dir.add_contact("Tom", "6543210987")

# Searching for a contact
search_name = "Alice"
print(telephone_dir.search_contact(search_name))

# Displaying all contacts
telephone_dir.display_all_contacts()
