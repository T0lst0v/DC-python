
number = ''
while number != 'q':
    try:
        number = int(input("Enter number: "))
        # if number == 'q':
        #     break
    except ValueError:
        print("Please enter the NUMBER!")
