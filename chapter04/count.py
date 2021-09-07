# Get number with highest count
# Most frequent integer in a list

from collections import defaultdict, Counter


def get_number_highest_count(counts):
    max_count = 0
    for number, count in counts.item():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    return get_number_highest_count(counts)


#  A pythonic approach


def get_number_highest_count(counts):
    max_count = 0
    for number, count in counts.item():
        if count > max_count:
            max_count = count
            number_with_highest_count = number
    return number_with_highest_count


def most_frequent(numbers):
    counts = defaultdict(int)
    for number in numbers:
        counts[number] += 1
    return get_number_highest_count(counts)


# Helper function for counting things: Counter
def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_highest_count(counts)


# Functional  programming

def get_number_with_highest_counts(counts):
    return max(
        counts, key=lambda number: counts[number]
    )


def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_highest_count(counts)
