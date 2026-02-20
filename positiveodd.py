n = int(input("Enter a number:"))
if(n>0):
    if(n%2==0):
        print(n,"is a positive even number")
    else:
        print(n,"is a positive odd number")
else:
    print(n,"is a negative number")