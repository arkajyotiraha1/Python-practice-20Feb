# check if 1st 2 are digits and then check if last 2 are alphabets
s = input("Enter a string:")
if s[:2].isdigit():
    if s[-2:].isalpha():
        print("Valid format")
else:
    print("Invalid format")
