import datetime

# from datetime import timedelta


# def total_time_played(start, finish):
#     total_time_played = datetime.datetime.combine(datetime.date.min, finish) - datetime.datetime.combine(datetime.date.min, start)
#     return total_time_played


# def current_time():
#     time = datetime.datetime.now().time()
#     return time


# time = datetime.datetime.now().time()
# total = total_time_played(time, current_time())

# print(total.seconds)

# print(":".join(str(total).split(":")[:2]))

# t = ":".join(str(total).split(":")[:2])
# print(type(t))

# total -


# def total_time_format_int(total):
#     minutes = total.seconds / 60
#     return minutes
#     # hours, remainder = divmod(total, 3600)
#     # minutes, seconds = divmod(remainder, 60)
#     # print '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def date_to_var():
    date = datetime.datetime.now().strftime("%m-%d-%Y")
    # timestr = datetime.time.strftime("%Y-%m-%d")
    return date


t = date_to_var()
print(t)

with open(f"{date_to_var()}.txt", "a") as file:
    file.write("hey")
