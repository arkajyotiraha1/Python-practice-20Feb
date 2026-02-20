PIN = 713365
user_PIN = eval(input("Enter your ATM PIN:"))
if user_PIN == PIN:
    balance = eval(input("Enter your balance:"))
    withdrawal = eval(input("Enter the amount to withdraw:"))
    if withdrawal <= balance:
        print("Withdrawal successful. Remaining balance:", balance - withdrawal)
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")


