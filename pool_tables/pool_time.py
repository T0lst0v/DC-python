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


# returning difference between 2 time stamps in timeDelta type
def total_time_played(start, finish):
    total_time_played = datetime.datetime.combine(datetime.date.min, finish) - datetime.datetime.combine(datetime.date.min, start)
    return total_time_played


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


# Creating array with class Table
for i in range(1, 10):
    i = " " + str(i)
    pool_tables_arr.append(PoolTables(i))
for i in range(10, total_tables + 1):
    pool_tables_arr.append(PoolTables(i))


# ----- Start -- -----
print_all_tables()
while user_choice != "q":
    print("")
    user_choice = input("------ what next?: ")

    if user_choice == "?":
        print(options)  # in case if there are more options for specific use for Admin

    # display all tables
    if user_choice == "0":
        print_all_tables()

    # check in Table
    if user_choice == "1":
        print_all_tables()
        print("")
        choice_table = input("------ What table to Check In?: ")
        if choice_table != "q" and choice_table.isnumeric() == True:
            if choice_table.isnumeric():
                i = int(choice_table)
                # only existing tables
                if i not in range(1, total_tables + 1):
                    print("")
                    print(f"~~~~~~~~~~~~~ There is no table {i} ~~~~~~~~~~~~~~~")
                else:
                    i -= 1
                    if pool_tables_arr[i].availability == True:
                        pool_tables_arr[i].start_time = current_time()  # datetime.datetime.now().time()
                        pool_tables_arr[i].availability = False
                        print_all_tables()
                    else:
                        print_all_tables()
                        print(f"~~~~~~~~~ Sorry table {choice_table} is not Availabele ~~~~~~~~")

        # wrong character
        elif choice_table != "q" and choice_table.isnumeric() == False:
            print_all_tables()
            print(not_number_msg)

        # back to loop
        elif choice_table == "q":
            print_all_tables()
            choice_table = " "  # changing  previous value 'q' so would still stay in a loop

    # checkout table
    if user_choice == "2":
        print_all_tables()
        print("")
        choice_table = input("------ What Table to Check Out?: ")

        # only if table is Occupied
        if choice_table != "q" and choice_table.isnumeric() == True:
            i = int(choice_table) - 1
            if pool_tables_arr[i].availability == False:
                pool_tables_arr[i].end_time = current_time()
                pool_tables_arr[i].availability = True
                pool_tables_arr[i].total_time_played = total_time_played(pool_tables_arr[i].start_time, pool_tables_arr[i].end_time)

                # write to the file
                with open(f"{today_date_to_str()}.txt", "a") as file:
                    file.write(f"Table {pool_tables_arr[i].table_number}")
                    file.write("\n")
                    file.write(f" from {pool_tables_arr[i].start_time} to {pool_tables_arr[i].end_time}")
                    file.write("\n")
                    file.write(f" total {pool_tables_arr[i].total_time_played}")
                    file.write("\n")
                print_all_tables()

                # price out
                price = pricing_per_game(pool_tables_arr[i].total_time_played, pool_tables_arr[i].price)
                print(f"++++[ price is - ${price} | time played - {total_time_format_str(pool_tables_arr[i].total_time_played)} ]+++++")

            # if it is not Occupied
            elif pool_tables_arr[i].availability == True:
                print_all_tables()
                print("~~~~~~~~~~ This table wasn't Occupied  ~~~~~~~~~~")

        # wrong character

        elif choice_table != "q" and choice_table.isnumeric() == False:
            print_all_tables()
            print(not_number_msg)
        # back to loop
        elif choice_table == "q":
            print_all_tables()
            choice_table = " "  # changing  previous value 'q' so would still stay in a loop

print("")
print("Have a Good Day!")
print("")
