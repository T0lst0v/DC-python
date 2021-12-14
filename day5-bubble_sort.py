# Bubble Sort

numbers = [2, 1, 45, 67, 89, 4, 5, 7, 9]

for i in range(0, len(numbers)):
    # print(f'max = {max}')
    for j in range(0, len(numbers)):
        print(f"i = {numbers[i]}, j = {numbers[j]}")
        if numbers[i] > numbers[j]:
            max = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = max
            print(f'max = {max}')
        print(f'max = {numbers[j]}')

print(numbers)
