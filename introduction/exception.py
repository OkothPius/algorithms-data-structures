import math

a_number = int(input('Please enter an integer '))
try:
    print(math.sqrt(a_number))
    if a_number <= 0:
        raise ValueError("Enter a whole number")
except ValueError as ve:
    print("Enter a Whole Integer")
    print("Using absolute value instead")
    print(math.sqrt(abs(a_number)))