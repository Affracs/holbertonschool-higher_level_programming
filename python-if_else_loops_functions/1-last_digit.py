#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#finds last digit held in "number" and assign it to "last"
if number >= 0:
    last = number % 10
else:
    last = number % -10
    
#checks if last digit is >5, 0, or <6/ not 0
if last > 5:
    state_of_digit = "and is greater than 5"
elif last == 0:
    state_of_digit = "and is 0" 
else:
    state_of_digit = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {state_of_digit}")
