from datetime import datetime


def day():
    return datetime.now().strftime("%A")


def part_of_day():
    current_hour = datetime.now().hour

    if current_hour < 12:
        part_of_day = "morning"
    elif 12 <= current_hour < 17:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"
    return part_of_day


# Referencing extracted function inside class
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        print(f"Hi {self.name}, welcome to {store}! ")
        print(f"\tHow's your {day()} {part_of_day()} going? ")
        print("\tHere's a coupon for 20% off!")


# Instantiating the class with name attribute
greeting = Greeter("Petter")
greeting.greet("best buy")
