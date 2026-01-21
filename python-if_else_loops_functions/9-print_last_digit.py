#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if last < 0:
        last = -last
    print("{}".format(last), end="")
    return last
