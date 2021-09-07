# reading the whole file in as a list of rows

color_count = {}

with open("all-favorite-colors.txt") as favortite_colors_file:
    favorite_colors = favortite_colors_file.read().splitlines()

for color in favorite_colors:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1


# Updating the code to rad one line from the file at a time

color_count = {}

with open("all-favorite-colors.txt") as favortite_colors_file:
    for color in favortite_colors_file:
        color = color.strip()

        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

# Using Pythons's features to minimize space
all_colors = set()

with open('all-favorite-colors.txt') as favorite_colors_file:
    for line in favorite_colors_file:
        all_colors.add(line.strip())

print('Amber Waves of Grain' in all_colors)
