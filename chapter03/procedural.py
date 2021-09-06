NAMES = ['Abby', 'Dave', 'Keira']


def print_greetings():
    greeting_pattern = 'Say hi to {name}!'
    nice_person_pattern = '{name} is a nice person!'
    for name in NAMES:
        print(greeting_pattern.format(name=name))
        print(nice_person_pattern.format(name=name))


# Lets calculate the sum of numbers


def calculate_total(sample_list):
    return sum([num for num in sample_list1])


sample_list1 = [10, 20, 30, 40]
sample_list2 = [10, 20, 30, 40]

print(calculate_total(sample_list1))
print(calculate_total(sample_list2))
