# ----------------------
# Write a Python program to calculate the value of 'a' to the power 'b'.
# Test Data :
# (power(3,4) -> 81

number = int(input('enter number: '))
power_of = int(input('to power of: '))


def power(a, b):
    const = a
    for i in range(1, b):
        a = a * const
    return(a)


print(power(number, power_of))
