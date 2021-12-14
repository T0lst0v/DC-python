# Write a program that calculate the number of vowels used in a sentence.
# Example:
#     input = "The elephant is walking in the enclosure!"
#     Output:
#     e = 5
#     a = 2
#     i = 2

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']
user_sentence = input('enter the sentence: ')


for i in range(len(vowels)):
    v = 0
    for j in range(len(user_sentence)):
        if vowels[i] == user_sentence[j]:
            v = v + 1
    print(f'{vowels[i]} = {v}')
