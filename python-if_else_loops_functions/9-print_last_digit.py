#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the last digit regardless of sign
    print(last_digit, end="")  # Print without newline at the end
    return last_digit
