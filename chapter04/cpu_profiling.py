# from timeit import timeit
# setup = "from datetime import datetime"
# statement = "datetime.now()"
# result = timeit(setup=setup, stmt=statement)

# print(f"Took an average of {result}ms")


# Profiling the CPU performance of a Python program

import random
import time


# def an_expensive_function():
#     execution_time = random.random()/100
#     time.sleep(execution_time)


# if __name__ == "__main__":
#     for _ in range(1000):
#         an_expensive_function()


# Try it out


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()


def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()


if __name__ == '__main__':
    sort_expensive()
    for i in range(1000):
        sort_cheap()
