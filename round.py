#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: December 2019
# This program uses an array

import random


def main():
    # function holds list

    # variables
    numbers = []
    total = 0

    # input
    print("numbers are: ")
    for loop_c in range(0, 9):
        single_number = random.randint(0, 100)
        numbers.append(single_number)
        print("{}".format(single_number))
    print("")
    for loop_2 in range(0, 9):
        total += numbers[loop_2]
    final = total / 10
    print("average = {}".format(final))


if __name__ == "__main__":
    main()
