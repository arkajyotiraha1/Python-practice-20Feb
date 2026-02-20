# first half and second half sum of a list
l = eval(input("Enter a list of numbers:"))
mid = len(l) // 2
first_half_sum = sum(l[:mid])
second_half_sum = sum(l[mid:])
if(first_half_sum > second_half_sum):
    print("First half greater")
elif(first_half_sum == second_half_sum):
    print("Equal halves")
else:       
    print("Second half greater")
