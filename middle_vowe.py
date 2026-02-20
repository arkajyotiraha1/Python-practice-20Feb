# if length of string is greater than 5 then check if the middle character is a vowel
s = input("Enter a string:")
if len(s) > 5:  
    mid = len(s) // 2
    if s[mid].lower() in 'aeiou':
        print("Middle character is a vowel")
    else:
        print("Middle character is not a vowel")
else:
    print("String too short")  
