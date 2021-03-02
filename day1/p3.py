# Program to find sum of digits 

number = int(input("Enter a number to find sum of digits in it: "))
tempNum = number
sum = 0
while number != 0:
    remainder = number % 10
    number = number // 10
    sum += remainder

print("The sum of digits in ",tempNum," is : ",sum)