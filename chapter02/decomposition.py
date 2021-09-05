# Suppose you are creating a fan site for the Three Stooges

# Initial Implementation
names = ["Larry", "Curly", "Moe"]
message = "The Three Stooges: "

for index, name in enumerate(names):
    if index > 0:
        message += ", "
    if index == len(names) - 1:
        message += " and "
    message += name
# print(message)

# Repitition

names = ["Moe", "Larry", "Shemp"]
message = "The Three Stooges: "

for index, name in enumerate(names):
    if index > 0:
        message += ", "
    if index == len(names) - 1:
        message += "and "
    message += name
# print(message)


# Extracting the introductory logic in a function to reduce repetition


def introduce_stooges(names):
    message = "The Three Stooges: "

    for index, name in enumerate(names):
        if index > 0:
            message += ", "
        if index == len(names) - 1:
            message += " and "
        message += name
    return message


introduce_stooges(["Larry", "Curly", "Moe"])
introduce_stooges(["Moe", "Larry", "Shemp"])

# At this point, it turns out the function has two concerns
# - Knowing the introduction is for the Three Stooges
# - Introducing a list of names at the stooges


# Shooting for one concern

def introduce(title, names):
    message = f"{title}: "

    for index, name in enumerate(names):
        if index > 0:
            message += ", "
        if index == len(names) - 1:
            message += "and "
        message += name
    return message


introduce("The Three Idiots", ["Rajan", "Rancho", "Panchan"])
introduce("The Three Stooges", ["Moe", "Larry", "Shemp"])


# Extract Further


def join_names(names):
    name_string = ""

    for index, name in enumerate(names):
        if index > 0 and len(names) > 2:
            name_string += ","
        if index > 0:
            name_string += " "
        if index == len(names) - 1 and len(names) > 1:
            name_string += "and "
        name_string += name
    return name_string


def introduce(title, names):
    print(f"{title}: {join_names(names)}")


introduce("The Three Idiots", ["Rajan", "Pachan"])
