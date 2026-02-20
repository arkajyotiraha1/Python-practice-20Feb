# repeatedly sum digits until single digit obtained
n = int(input("Enter a number:"))
while n >= 10:
    sum_digits = 0
    while n > 0:
        digit = n % 10
        sum_digits += digit
        n //= 10
    n = sum_digits
print(sum_digits)








    