# You are responsible for creating an app that manages groceries.
# Your groceries are characterized by Shopping Lists
# which can contain grocery items. Here are the features you need to implement:
#   You need to ask the user for the input.
#   A user should be able to create a shopping list.
#   A shopping list consists of a title and address.

#         Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc

#   A user should be able to add multiple shoppings lists
#   Give user an option to display the list
#   A user should be able to add a grocery items to a particular shopping list.
#   A grocery item consists of a title, price, quantity.

#         Example Milk, Cookies, Paper, Napkins, Soda, Chips etc

# Fiesta
# Milk, Soda, Fish
# Walmart
# Paper, Napkins, Plate, Chips
# Sams Club
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey

class Groceries():
    def __init__(self, title, amount, price):
        self.title = title
        self.amount = amount
        self.price = price


class Stores():
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.inventory = []

    def add_item(self, title, amount, price):
        self.inventory.append(Groceries(title, amount, price))

    def print_all_inventory(self):
        i = 1
        for item in self.inventory:
            print(f'{i}. {item.title} - {item.amount} ${item.price}')
            i += 1

    def print_all(self):
        print(f'{self.title}')
        print(f'{self.address}')
        self.print_all_inventory()


def indexed_store_title():
    i = 1
    for item in all_stores:
        print(f'{i}. {item.title}')
        i = i+1


all_stores = []
options_memo = ('''
====================
1 - Create New List
2 - Add to the Existing list
3 - delete list
4 - delete from the list
5 - show all
q - quit
? - this memo
====================
''')

print(options_memo)
user_choice = ''
new_store = 'test'

while user_choice != 'q':
    print(' ')
    user_choice = input('what next?: ')
    if user_choice == '?':
        print(options_memo)
# Create New List
    elif user_choice == '1':
        user_title = input('enter name of the store: ')
        user_address = input('enter address of the store: ')
        new_store = Stores(user_title, user_address)
        all_stores.append(new_store)

# loop for adding items(inventory) to created Store
        user_item = ''
        while user_item != 'q':
            user_item = input('enter Grocery or q to quit: ')
            if user_item != 'q':
                user_item_amount = int(input('enter amount of it : '))
                user_item_price = float(input('enter price of it: '))

                new_store.add_item(
                    user_item, user_item_amount, user_item_price)

# Add to the Existing list
    elif user_choice == '2':
        indexed_store_title()
        user_list_choice = input(
            'to what list number you want to add items?: ')
        if user_list_choice == 'q':
            print(' ')
            user_choice = input('what next?: ')
        else:
            user_list_choice = int(user_list_choice)
            user_item = input('enter Grocery or q to quit: ')
            user_item_amount = int(input('enter amount of it : '))
            user_item_price = float(input('enter price of it: '))

            chosen_store = all_stores[user_list_choice-1]
            chosen_store.add_item(user_item, user_item_amount, user_item_price)

            print('Added')

# Delete Specific Store form the list
    elif user_choice == '3':
        indexed_store_title()

        user_list_choice = input('what list number to delete?: ')
        if user_list_choice != 'q':
            user_list_choice = int(user_list_choice)
            print('in process')
            del(all_stores[user_list_choice-1])

# Delete Item from chosen store
    elif user_choice == '4':
        indexed_store_title()
        user_store_choice = input(
            'in what list you would like to delete items: ')
        if user_store_choice != 'q':
            user_store_choice = int(user_store_choice)

            all_stores[user_store_choice-1].print_all()
            user_choice_item = int(
                input('what item # you would like to delete: '))
            del(all_stores[user_store_choice-1].inventory[user_choice_item-1])

        print('---- Deleted -----')


# Print All
    elif user_choice == '5':
        print(' ')
        for item in all_stores:
            item.print_all()
            print('----------')

print('Bey!')
