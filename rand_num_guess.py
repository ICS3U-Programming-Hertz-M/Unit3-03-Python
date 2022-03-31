#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: 28 mar 2022
# This program ask the user to guess any number between 0 and 9
import random


random_variable = random.randint(0, 9)


def main():
    # this function ask the user to guess a number
    guess_number = int(input("Guess_any_number from 0 to 9:"))
    print("")

    # compare the number entered to the random number
    if guess_number == random_variable:
        print("correct guess!")
    else:
        print("your guess is incorrect,the correct guess is", random_variable)


if __name__ == "__main__":
    main()
