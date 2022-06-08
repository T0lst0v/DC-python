# file  - read and write

# FILES

# WRITING
# open(name of the file, mode) By default mode is "r"

# w = Writing a file
# r = Reading a file
# a = Appending mode
# a+ = Appending and reading mode
# w+ = Writing and reading a file

# OPEN 1
# opening the file for writing, create a file if does not exist or overrite if exist
# file = open("todo.txt", "w")
# write text to a file
# file.write("Mow the lawn")
# file.write("Clean the car")
# ALWAYS close the file
# file.close()

# OPEN 2
# with operator is going to call close() automatically at the end of with body
# with open("todo.txt", "w") as file:
#  file.write("Do dishes")

# READING A FILE

# read all the contents of a file and return as string
# default mode is "r"
# with open("todo.txt") as file:
#  content = file.read()
#  print(content)

# readlines is going to return an array of lines in the file
# with open("todo.txt") as file:
#  lines = file.readlines()
#  print(lines)


# Activities:

# -----------------------

# with open('loop.txt', 'a') as file: # not a good solution as file being open for long time is a memory leak
#     while True:
#         text = input('what is your favorite dish?: ')
#         if text == 'q':
#             break
#         file.write(text)
#         file.write('\n')  # new line
#         # file.write('\r')  # return

# with open('loop.txt') as file:  # print out content of the file
#     content = file.read()
#     print(content)

# ----------------------

# while True:
#     friend_name = input("Enter your friend's name: ")
#     if friend_name == "q":
#         break

#     with open("friends.txt", "a") as file:
#         file.write(friend_name)
#         file.write("\n")

# with open("friends.txt") as file:
#     content = file.read()
#     print(content)


# -------------------

with open("emails.txt") as file:
    content = file.read().split(",")

print(content)
for item in content:
    print(item)


# ACTIVITY - DUPLICATE EMAILS

with open("emails.txt") as file:
    emails = file.read()

# convert string comma separated into an array
duplicate_emails = emails.split(", ")
# final array containing NO DUPLICATES
duplicate_free_emails = []

for email in duplicate_emails:
    if email not in duplicate_free_emails:
        duplicate_free_emails.append(email)

# print(duplicate_free_emails)

# OPTION 1
# write to the duplicate free emails text file
# with open("duplicate_free_emails.txt", "w") as file:
#  for email in duplicate_free_emails:
#    file.write(email)
#    file.write(",")

# OPTION 2
content = ",".join(duplicate_free_emails)
with open("duplicate_free_emails.txt", "w") as file:
    # join the contents of the array to make a comma separated string
    file.write(content)
