# classes
#
# class Customer():
#     def __init__(self, f_name, l_name):
#         self.first_name = f_name
#         self.last_name = l_name
#         self.full_name = f_name + " " + l_name


# customer = Customer('John', 'Doe')
# print(customer.full_name)

# -----------------------------------
# Create a class called BankAccount.
# Add properties for balance and account_number
# Allow the user to deposit funds to the account. This can be accomplished by adding a deposit function to the BankAccount class.
# Allow the user to withdraw funds from the account. This can be accomplished by adding a withdraw function to the BankAccount class.
# Allow the user to transfer funds between two accounts. This can be accomplished by adding a transfer_funds function to the BankAccount class.
# After creating the BankAccount class, along with all the functions make sure to create instance of BankAccount and perform actions.


# class BankAccount():
#     def __init__(self, a, b):
#         self.acc_numb = a
#         self.balance = int(b)

#     def deposit(self, x):
#         self.balance += x

#     def withdraw(self, x):
#         self.balance -= x

#     def transfer_from(self, from_acc, x):
#         self.deposit(x)
#         from_acc.withdraw(x)


# acc1 = BankAccount(1, 200)
# acc2 = BankAccount(2, 1000)

# print(acc1.acc_numb)
# print(acc1.balance)

# acc1.deposit(250)
# print(acc1.balance)

# acc1.transfer_from(acc2, 50)
# print(acc1.balance)
# print(acc2.balance)

# -----------
# Create a class called User which consists of (first_name, last_name) properties. Create a class name Address which consists of (street, city, state, zip_code) properties.

# Create a relationship between User and Address in a way a single user can have multiple addresses.
# Add a new method/function to User class called add_address(self, address) which would take an address as an argument and add it to a list/array of addresses.
# Add another method to the User class called display_addresses(self) which would display all the address of that user.


class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + ' ' + last_name
        self.addresses = []

    def add_address(self, addr):
        self.addresses.append(addr)


user1 = User("John", "Doe")
user1.add_address(Address("1200 Richmond", "Houston", "TX"))
user1.add_address(Address("456 Road", "Austin", "TX"))

print(user1.full_name)


def all_addresses(u):
    i = 1
    for addr in u.addresses:
        print(f'{i}. addres:')
        print(addr.street)
        print(f'{addr.city} {addr.state}')
        i += 1


all_addresses(user1)
#   --------------------
