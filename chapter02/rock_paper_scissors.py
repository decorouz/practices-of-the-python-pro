# Shoddy procedural code

import random


options = ['rock', 'paper', 'scissors']
print('(1) Rock\n(2) Paper\n(3) Scissors')


human_choice = options[int(input('Enter the number of your choice: ')) - 1]
print(f'You chose {human_choice}')


computer_choice = random.choice(options)
print(f'The computer chose {computer_choice}')


if human_choice == 'rock':
    if computer_choice == 'paper':
        print('Sorry, paper beat rock')
    elif computer_choice == 'scissors':
        print('Yes, rock beat scissors!')
    else:
        print('Draw!')
elif human_choice == 'paper':
    if computer_choice == 'scissors':
        print('Sorry, scissors beat paper')
    elif computer_choice == 'rock':
        print('Yes, paper beat rock!')
    else:
        print('Draw!')
elif human_choice == 'scissors':
    if computer_choice == 'rock':
        print('Sorry, rock beat scissors')
    elif computer_choice == 'paper':
        print('Yes, scissors beat paper!')
    else:
        print('Draw!')

# Code with extracted function

OPTIONS = ["rock", "paper", "scissors"]


def get_human_choice():
    choice_number = int(input("Enter the number of your choice: "))
    return OPTIONS[choice_number - 1]


def get_compueter_choice():
    return random.choice(OPTIONS)


def print_options():
    print("\n".join(f"({i + 1}) {option.title()}" for i,
          option in enumerate(OPTIONS)))


def print_choices(human_choice, computer_choice):
    print(f"You chose {human_choice}")
    print(f"The computer chose {computer_choice}")


def print_win_lose(human_choice, computer_choice, human_beats, human_lose_to):
    if computer_choice == human_lose_to:
        print(f"Sorry, {computer_choice} beats {human_choice} ")
    elif computer_choice == human_beats:
        print(f"Yes, {human_choice} beats {computer_choice}")


def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print("Draw")
    if human_choice == "rock":
        print_win_lose("rock", computer_choice, "scissors", "paper")
    elif human_choice == "paper":
        print_win_lose("paper", computer_choice, "rock", "scissors")
    elif human_choice == "scissors":
        print_win_lose("scissors", computer_choice, "paper", "rock")


print_options()
human_choice = get_human_choice()
computer_choice = get_compueter_choice()
print_choices(human_choice, computer_choice)
print_result(human_choice, computer_choice)
