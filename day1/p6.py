# Program to find sum of odd digit

number = int(input("Enter a number to find sum of odd digit : "))
tempNum = number
sum = 0
while number != 0:
    remainder = number % 10
    number = number // 10

    if(remainder % 2 != 0):
        sum +=  remainder

print("The sum of odd digits in ",tempNum," is : ",sum)