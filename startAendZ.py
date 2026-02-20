# starts with a and ends with z
s = input("Enter a string:")
if s.startswith('A'):
    if s.endswith('Z'):
        print("Valid AZ String")
    else:
        print("Starts with A but invalid end")
else:
    print("Invalid String")
