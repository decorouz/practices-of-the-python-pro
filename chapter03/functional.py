# Functional languages require youj think about programs as compositions of functions.
# for loops are replaced by function that operate on list

from functools import partial
from functools import reduce
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i * i)


# In functional programming

print(map((i)= > i*i, [1, 2, 3, 4, 5]))


squares = map(lambda x: x * x, [1, 2, 3, 4, 5])
should = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])


# The preference in Python would be the following:

squares = [x * x for x in [1, 2, 3, 4, 5]]
should = all([True, True, False])
evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]


# Partial functions
def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)
cube = partial(pow, power=3)
