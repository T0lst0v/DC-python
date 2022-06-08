# import json

# choice = ""
# users = []

# while choice != "q":
#     name = input("enter name: ")
#     age = input("enter age: ")
#     user = {"name": name, "age": age}
#     users.append(user)
#     choice = input("q to quit or Return to add more")
# with open("user.json", "w") as f:
#     json.dump(users, f)


# with open("user.json") as f:
#     users = json.load(f)


# for item in users:
#     print(f"{user[name]}  {user[age]}")


import json


with open("movies.json") as file:
    movies_dic = json.load(file)

    movies_arr = movies_dic["Search"]

for item in movies_arr:
    # type = item["Type"].upper()
    print(
        f"""{item['Title']}
 {item["Type"].title()} 
 year - {item['Year']} 
 imdbID - {item['imdbID']}
  """
    )
