"""Generators are constructs in Python that produce a single value at a time, pausing until the next value is requested"""


# Using yield to pausse and prepare

def range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start

    while current < stop:
        yield current
        current += 1


my_range = list(range(5, 10))


# Short generator that yields squared numbers

def square(items):
    for item in items:
        yield item ** 2


"""It is recommended to make use of generators over list whenever you can """
