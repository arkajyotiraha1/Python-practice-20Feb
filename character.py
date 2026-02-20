n = eval(input("Enter a character:"))
if n.isupper():
    print(n,"is a uppercase character")
elif n.islower():
    print(n,"is a lowercase character")
elif n.isdigit():
    print(n,"is a digit")
else:
    print("Special character")
