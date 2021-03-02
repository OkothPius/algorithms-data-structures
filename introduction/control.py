# counter = 1
# while counter <= 5:
#     print("Hey man!")
#     counter += 1


# for i in [1, 4, 6, 7]:
#     print(i)

word_list = ['cat', 'dog', 'rabbit']
letter_list = []

for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list: # No duplicates
            letter_list.append(a_letter)
print(letter_list)
