# Program to find count of digits in a number
number = int(input("Enter a number to find count of digits in it : "))
tempNum = number
count = 0
while number != 0:
    remainder = number % 10
    number = number // 10
    count += 1
    
print("The count of digits in ",tempNum," is : ",count)