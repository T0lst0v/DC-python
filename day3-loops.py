# friends = ["Name0", "Name1", "Name2", "Name3", "Name3", "Name4", "Name5"]

# for index in range(0, len(friends)):
#     print(friends[index])


# user_input = input('Enter the word: ')
# for i in range(0, len(user_input)):
#     print(user_input[(len(user_input)-1)-i])

# word = input("Enter word:")
# reversed_word = ""
# for index in range(len(word) -1, -1, -1):
#   reversed word += word[index]
#  #reversed word = reversed word + word[index]
# print (reversed word)

# #  -- Factorial
# user_input = int(input('Enter the number: '))
# i = 1
# result = user_input

# while i != user_input:
#     result = result * (user_input - i)
#     i = i + 1

# print(f'Factorial of number {user_input} is {result} ')

#  -- Palindrome

user_input = input('Enter the word to see if it is a  Polindrome: ')


def polindreom(word):
    user_input_reverse = ''
    for i in range(0, len(user_input)):
        user_input_reverse += user_input[(len(user_input)-1)-i]

    if user_input_reverse == user_input:
        return True
    else:
        return False
#   return word == reversed_word #short veersion of previous if comparison


print(polindreom(user_input))
# -- Prime or Not
# user_input = int(input('Enter the Number: '))

# if user_input == 0:
#     print('Number is 0')
# elif user_input == 1 or user_input == 2:
#     is_it_prime = True

# i = 2
# while (i <= 9) and (i != user_input):
#     is_it_prime = True
#     if user_input % i == 0:
#         is_it_prime = False
#         break
#     i += 1

# if is_it_prime == True:
#     print(f'{user_input} is a Prime Number')
# else:
#     print(f'{user_input} is Not a prime number')


# Write an app which sums integers in an array.
# Example: [4,5,6,71]
# Answer: 86
