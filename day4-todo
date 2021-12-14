# ---------------------------------------------------
# TodoList Using Dictionaries
# In this assignment you are going to create a TODO app.
# When the app starts it should present user with the following menu:
#     Press 1 to add task
#     Press 2 to delete task
#     Press 3 to view all tasks
#     Press q to quit
# The user should only be allowed to quit when they press 'q'.

# Add Task:
#     Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low.

# Delete Task:
#     Show user all the tasks along with the index number of each task. User can then enter the index number of the task to delete the task.

# View all tasks:
#     Allow the user to view all the tasks in the following format:
#     1 - Wash the car - high
#     2 - Mow the lawn - low


# Store each task in a dictionary and use 'title' and 'priority' as keys of the dictionary.
# Store each dictionary inside an array. Array will represent list of tasks.

#

# function for to print only specific priority
def print_priority(user_input, y, yy, arr, message):        # optional
    if (user_input == y) or (user_action == yy):            # optional
        print(" ")                                          # optional
        print(message)                                      # optional
        for d in arr:                                       # optional
            if d["priority"] == yy:                         # optional
                print(d['title'])                           # optional


task_arr = []
user_priority = ''
user_action = ''
options = [' ',
           '-------------------',
           '1 to Add task',
           '2 to Delete task',
           '3 to view All tasks',
           'q to quit',
           '-------------------',
           ' '
           ]

while user_action != "q":
    for i in range(len(options)):
        print(options[i])
    user_action = input('what next?: ')

    if user_action == "1":
        print(' ')
        print('Adding new Tsk:')
        user_task = input('enter Title: ')
        print(" ")
        print('h - hight, m - medium, l - low')
        user_priority = input('enter Priority: ')

        if user_priority == "h":          # optional
            user_priority = "hight"       # optional
        elif user_priority == 'm':        # optional
            user_priority = 'medium'      # optional
        elif user_priority == 'l':        # optional
            user_priority = 'low'         # optional

        task = {'title': user_task, 'priority': user_priority}
        task_arr.append(task)

    elif user_action == "2":
        print(' ')
        print("List of tasks:")
        for i in range(len(task_arr)):
            print(
                f"{i+1}. {task_arr[i]['title']}")
        user_action = input(
            'what task Number need to be Deleted: ')

        if user_action.isnumeric():                 # optional

            user_action = int(user_action)          # <- tab
            del(task_arr[user_action-1])            # <- tab

    elif user_action == "3":
        print(' ')
        print("List of tasks:")
        for i in range(len(task_arr)):
            print(
                f"{i+1} - {task_arr[i]['title']} - {task_arr[i]['priority']}")

        print(' ')                                               # optional
        user_action = input('what priority to show only?: ')     # optional
        print_priority(user_action, "h", "hight", task_arr,      # optional
                       "All Hight priority tasks:")              # optional
        print_priority(user_action, "m", "medium", task_arr,     # optional
                       "All Medium priority tasks:")             # optional
        print_priority(user_action, "l", "low", task_arr,        # optional
                       "All Low priority tasks:")                # optional

        # elif (user_action == 'm') or (user_action == 'medium'):
        #     print(" ")
        #     print("All Medium priority tasks")
        #     for d in task_arr:
        #         if d["priority"] == 'medium':
        #             print(d['title'])

        # function :

        # def print_priority(user_input, y, yy, arr, message):
        #     if (user_input == y) or (user_action == yy):
        #         print(" ")
        #         print(message)
        #         for d in arr:
        #             if d["priority"] == yy:
        #                 print(d['title'])
