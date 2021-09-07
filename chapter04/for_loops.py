names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    print(name)

# Multiple steps inside the loop
names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    greeting = 'Hi, my name is'
    print(f'{greeting} {name}')

# Loop over the same list a set number okf times
names = ['Aliya', 'Beth', 'David', 'Kareem']
for name in names:
    print(f'This is {name}!')

message = 'Let\'s welcome '
for name in names:
    message += f'{name} '
print(message)


# Nested loops

def has_duplicate(sequence):
    for index1, item1 in enumerate(sequence):
        for index2, item2 in enumerate(sequence):
            if item1 == item2 and index1 != index2:
                return True
    return False
