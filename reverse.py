# reverse a number using while loop and check whether the rerversed number is greater than it or not
n = int(input("Enter a number:"))
reverse = 0
temp = n
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if(n<reverse):
    print("Reversed number is greater")
else:
    print("Reversed number is smaller")
