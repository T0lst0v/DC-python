# You have just been hired by University of Houston as a developer.
# Your first task is to create a pool table management app
# which will manage the pool tables in University Center Games Room.

# Here are the requested features:
#     As an admin you should be able to see all the tables (12)
#     As an admin each table in the list should show, whether the table is OCCUPIED
#       or NOT OCCUPIED.
#     As an admin if the table is OCCUPIED then show the start time of the table,
#       number of minutes played.
#       (Hardmode - If the minutes are > 60 then show them in terms of hours)
#     As an admin you can only give out the tables that are NOT OCCUPIED.
#       This means if pool table 8 is occupied and you try to give it out
#       then the app will print a message saying
#       "Pool Table 8 is currently occupied".
#    As an admin whenever I close the table it should write an entry
#       in the text file / json file. The file should be named
#       in the following format:
#           (11-22-2017.txt or 11-22-2017.json)
#       keeping track of all the tables.
#
# The entry can consists of the following information:

#   Pool Table Number
#   Start Date Time
#   End Date Time
#   Total Time Played
#   Cost (if you are doing the hard mode)

# HARD MODE - Associate dollar amount for time played on the pool table. $30 per hour.
# MORE HARD MODE - Write Unit Tests for your application

import datetime


# Variables
price = 0.0
pool_tables_arr = []
user_choice = ""
total_tables = 12
# current_time = datetime.datetime.now().time()
# today_date = datetime.date.today()
options = """==================================================
1 - Check In                              q - quit 
2 - to Check Out                          0 - All
================================================== """
not_number_msg = """~~~~~~~~~~~~~~ that wasn't a NUMBER ~~~~~~~~~~~~~~"""


class PoolTables:
    def __init__(self, table_number):
        self.table_number = table_number
        self.start_time = None
        self.end_time = None
        self.availability = True
        self.total_time_played = 0
        self.price = 32


# printing Spreadsheet of tables and Option Menu
def print_all_tables():
    print("")
    print("==================[Pull Tables]==================")
    for item in pool_tables_arr:
        table = item.table_number
        avail = item.availability
        total = item.total_time_played
        start = item.start_time
        print("-------------------------------------------------")
        if avail == False:  # print more info of Occupied tables
            total = total_time_played(start, current_time())
            total = total_time_format_str(total)
            start = time_format_string(start)
            print(f"{table}. {is_avail(avail)} started [ {start} ] duration [ {total} ]")
        else:
            print(f"{table}. {is_avail(avail)}")

    print(options)


# print Available/Occupied instead True/False
def is_avail(x):
    if x == True:
        return "Available"
    else:
        return "Occupied "


# return current time
def current_time():
    time = datetime.datetime.now().time()
    return time


# returning formated time as a string not working on total_time(timedelta)
def time_format_string(t):
    time_format = t.strftime("%H:%M")
    return time_format


# returning formated time for total(timedelta) as a STRING
def total_time_format_str(t):
    total = ":".join(str(t).split(":")[:2])
    return total


# returning Minutes for total(timedelta) as Float
def total_time_min(total):
    minutes = total.seconds / 60
    return minutes


# returns cost per minutes played (type float)
def pricing_per_game(t, p):
    t = total_time_min(t)
    price = (p / 60) * t
    return "%.2f" % price


# returns today Date as a string
def today_date_to_str():
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    return date


# returning difference between 2 time stamps in timeDelta type
def total_time_played(start, finish):
    total_time_played = datetime.datetime.combine(datetime.date.min, finish) - datetime.datetime.combine(datetime.date.min, start)
    return total_time_played


# Creating array with class Table and its number
for i in range(1, 10):
    i = " " + str(i)
    pool_tables_arr.append(PoolTables(i))
for i in range(10, total_tables + 1):
    pool_tables_arr.append(PoolTables(i))

# printing a menu
print_all_tables()
while user_choice != "q":
    print("")
    user_choice = input("what next: ")
    if user_choice == "?":
        print(options)

    # display all tables
    if user_choice == "0":
        print_all_tables()

    # check in Table
    if user_choice == "1":
        print_all_tables()
        print("")
        choice_table = input("What table to Check In?: ")
        if choice_table != "q" and choice_table.isnumeric() == True:
            if choice_table.isnumeric():
                i = int(choice_table)
                if i not in range(1, total_tables + 1):  # only existing tables
                    print("")
                    print(f"There is no table {i}")
                else:
                    i -= 1
                    if pool_tables_arr[i].availability == True:
                        pool_tables_arr[i].start_time = current_time()  # datetime.datetime.now().time()
                        pool_tables_arr[i].availability = False
                        print_all_tables()
                    else:
                        print_all_tables()
                        print(f"~~~~~~~~~ Sorry table {choice_table} is not Availabele ~~~~~~~~")
        elif choice_table != "q" and choice_table.isnumeric() == False:
            print_all_tables()
            print(not_number_msg)
        elif choice_table == "q":
            print_all_tables()
            choice_table = " "  # with value 'q' it would still stay in a loop

    # checkout table
    if user_choice == "2":
        print_all_tables()
        print("")
        choice_table = input("What Table to Check Out?: ")
        if choice_table != "q" and choice_table.isnumeric() == True:
            i = int(choice_table) - 1
            if pool_tables_arr[i].availability == False:  # only if it is Occupied
                pool_tables_arr[i].end_time = current_time()
                pool_tables_arr[i].availability = True
                pool_tables_arr[i].total_time_played = total_time_played(pool_tables_arr[i].start_time, pool_tables_arr[i].end_time)

                price = pricing_per_game(pool_tables_arr[i].total_time_played, pool_tables_arr[i].price)
                # write to the file
                with open(f"{today_date_to_str()}.txt", "a") as file:
                    file.write(f"Table {pool_tables_arr[i].table_number}")
                    file.write("\n")
                    file.write(f" from {pool_tables_arr[i].start_time} to {pool_tables_arr[i].end_time}")
                    file.write("\n")
                    file.write(f" total {pool_tables_arr[i].total_time_played}")
                    file.write("\n")
                print_all_tables()
                print(f"++++[ price is - ${price} | time played - {total_time_format_str(pool_tables_arr[i].total_time_played)} ]+++++")
            # if it is not Occupied
            elif pool_tables_arr[i].availability == True:
                print_all_tables()
                print("~~~~~~~~~~ This table wasn't Occupied  ~~~~~~~~~~")
        elif choice_table != "q" and choice_table.isnumeric() == False:
            print_all_tables()
            print(not_number_msg)
        elif choice_table == "q":
            print_all_tables()
            choice_table = " "  # with value 'q' it would still stay in a loop

print("")
print("Have a Good Day!")
print("")
