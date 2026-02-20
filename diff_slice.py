# compare 1st 2 and last 2 characters of a list
l = eval(input("Enter a list of numbers:"))
if len(l) % 2 == 0:
    if l[:2] == l[-2:]:
        print("Slices with same elements")
    else:
        print("Slices are different")
else:
    print("Odd length list")
