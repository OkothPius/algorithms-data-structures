sq_list = []
for x in range(1, 11):
    sq_list.append(x*x)

print(sq_list)

## List comprehension
sq_list = [x*x for x in range(1, 10)]
sq_list = [x*x for x in range(1, 10) if x % 2 != 0]

character_list = [ch.upper() for ch in 'comprehension' if ch not in 'aeiou']

print(sq_list)
print(character_list)
