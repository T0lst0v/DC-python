# Return the number of perfect squares (like 4, 16, 25, 36, etc.) between two integers a and b, inclusive

# A perfect square is an integer that is the square of an integer;
# in other words, it is the product of some integer with itself.
# For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# the logic is  i from 1 to end_number keep multiplying on its self and check results if it is in range


first_number = int(input('Enter start point: '))
end_number = int(input('enter ending: '))

number_of = 0
i = 1
while i*i <= (end_number):
    if (i*i) in range(first_number, end_number+1,):
        print(f'{i*i} is perfect square ')
        number_of = number_of + 1
    i = i+1

print(f'total perfect squares is  {number_of}')
