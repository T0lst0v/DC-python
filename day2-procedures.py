# -- class Assignment 1
# Hello, My name is FirstName, LastName

# first_name = input("Enter you Name: ")
# last_name = input("Enter you Last Name: ")
# print(f"Hello, My name is {first_name}, {last_name}")


# def greet (name, age):
#     print (f'Hello {name}! you are {age}')

# greet('John', 30)

# -- class Assigment 2
# In this activity, you will ask for user input.
# User will enter a single character and your app will determine if that character is a vowel or not
# user_input = input('enter one letter: ')

# if (user_input == 'a' or user_input == 'A' or user_input == 'e' or user_input == 'E' or user_input == 'i' or user_input == 'I' or user_input == 'o' or user_input == 'O' or user_input == 'u' or user_input == 'U' or user_input == 'y' or user_input == 'Y' or user_input == 'w' or user_input == 'W'):
#     print('This is Vowel')
# else:
#     print('NOT a Vowel')

# -- class Assignment 3
# In this optional assignment you are going to ask the user for the two inputs as shown below:
# Enter the total amount
# Enter the tip percentage amount
# After the user has entered both inputs the application calculates the tip amount and displays it to the user.

# user_amount = float(input('Enter full amount: '))
# user_percnt = float(input('Enter %: '))


# def tip(mnt, prcnt):
#     result = mnt * prcnt / 100
#     return result

# print(tip(user_amount, user_percnt))


# -- home Assignment1
# In this assignment you are going to build a calculator. You are going to take three inputs from the user.
# Input 1 - Represents the first number
# Input 2 - Represents the operand (+, - , * , /)
# Input 3 - Represents the second number
# Based on the operand you are going to perform the math operation and print the result on the terminal.

# def sum(a, b):
#     return a+b


# def min(a, b):
#     return a-b


# def mult(a, b):
#     return a*b


# def div(a, b):
#     return a/b


# first_numb = float(input('enter 1st number: '))
# math_sign = input('enter opernad: ')
# second_numb = float(input('enter 2nd number: '))

# if math_sign == '+':
#     result = sum(first_numb, second_numb)
# elif math_sign == '-':
#     result = min(first_numb, second_numb)
# elif math_sign == '/':
#     result = div(first_numb, second_numb)
# elif math_sign == '*':
#     result = mult(first_numb, second_numb)

#  print(result)

# -- 2nd option

# first_numb = float(input('enter 1st number: '))
# math_sign = input('enter opernad: ')
# second_numb = float(input('enter 2nd number: '))

# if math_sign == '+':
#     result = first_numb + second_numb
# elif math_sign == '-':
#     result = first_numb - second_numb
# elif math_sign == '/':
#     result = first_numb / second_numb
# elif math_sign == '*':
#     result = first_numb * second_numb

# print(result)

# --home Assignment 2 - Even Odd
# Write an app which ask user for an input and then displays a message indicating whether the number is even or odd.


# numb = int(input('enter a number: '))

# if numb == 0:
#     print(numb, ' number is 0 ')
# elif (numb % 2) == 0:
#     print(numb, ' is even')
# elif (numb % 2) != 0:
#     print(numb, ' is odd')


# Assignment 3: Write a Fizz Buzz application.
# Take input from the user. If the input is divisible by 3 then print "Fizz", if the input it divisible by 5 then print "Buzz". If the input is divisible by 3 and 5 then print "Fizz Buzz".

numb = int(input('Enter Number: '))

if numb == 0:
    print('it is 0')
elif (numb % 5 == 0) and (numb % 3 == 0):
    print('FizzBazz')
elif numb % 3 == 0:
    print('Fizz')
elif numb % 5 == 0:
    print('Buzz')
else:
    print({numb}, ' not FizzBazz')
