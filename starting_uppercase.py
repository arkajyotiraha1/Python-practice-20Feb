# starts with uppercase and ends with lowercase
s = input("Enter a string:")
if s[0].isupper():
    print("Starts with uppercase")
elif s[-1].islower():
    print("Ends with lowercase")
else:
    print("Other case")
