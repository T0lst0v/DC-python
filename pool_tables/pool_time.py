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

                # only check in existing tables
                if i not in range(1, total_tables + 1):
                    print("")
                    print(f"~~~~~~~~~~~~~ There is no table {i} ~~~~~~~~~~~~~~~")
                else:
                    i -= 1
                    if pool_tables_arr[i].availability == True:
                        pool_tables_arr[i].start_time = current_time()  # datetime.datetime.now().time()
                        pool_tables_arr[i].availability = False

                        # write only starting time to the file
                        with open(f"{today_date_to_str()}.txt", "a") as file:
                            file.write(f"s-Table {pool_tables_arr[i].table_number}")
                            file.write("\n")
                            file.write(f" started at {pool_tables_arr[i].start_time}")
                            file.write("\r")
                            file.write("\r")

                        print_all_tables()
                    # if table was already checked in
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

        # only check out if table is Occupied
        if choice_table != "q" and choice_table.isnumeric() == True:
            i = int(choice_table) - 1
            if pool_tables_arr[i].availability == False:
                pool_tables_arr[i].end_time = current_time()
                pool_tables_arr[i].availability = True
                pool_tables_arr[i].total_time_played = total_time_played(pool_tables_arr[i].start_time, pool_tables_arr[i].end_time)

                # write start, end, duration time to the file
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
