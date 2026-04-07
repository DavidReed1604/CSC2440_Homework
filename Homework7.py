phonebook = {}
def add_entry(name, phone_number):
    phonebook[name] = phone_number
    print(f"{name} added successfully.")
def search_entry(name):
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
        return phonebook[name]
    else:
        print(f"{name} not found in phonebook.")
        return None
def delete_entry(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} not found in phonebook.")