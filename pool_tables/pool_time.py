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

from modules import *

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
