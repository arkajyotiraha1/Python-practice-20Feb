# check palindrome
n = int(input("Enter a Number:"))
reverse = 0
temp = n
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if(reverse == n):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")