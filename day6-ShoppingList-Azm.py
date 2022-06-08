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

shopping_lists = []


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.items = []

    def add_item(self, item):
        self.items.append(item)


while True:

    print("1. Add Shopping List: ")
    print("2. View All Shopping List: ")
    print("3. Add Item to a Shopping List: ")
    print("q: Quit: ")

    choice = input("Enter a selection: ")

    if choice == "1":
        title = input("Enter name of shopping list: ")
        address = input("Enter shopping list address: ")
        # object/instance of shopping list
        shopping_list = ShoppingList(title, address)
        shopping_lists.append(shopping_list)
    elif choice == "2":
        # display all shopping list
        for index in range(len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index + 1} - {shopping_list.title}")
            for item in shopping_list.items:
                print(item.name)

    elif choice == "3":
        # display all shopping list
        for index in range(len(shopping_lists)):
            shopping_list = shopping_lists[index]
            print(f"{index + 1} - {shopping_list.title}")
        shopping_list_index = int(
            input("Enter shopping list number to add items to: "))
        shopping_list = shopping_lists[shopping_list_index - 1]
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        grocery_item = Item(item_name, item_price)
        # shopping_list.items.append(grocery_item)
        shopping_list.add_item(grocery_item)

    elif choice == "q":
        break
