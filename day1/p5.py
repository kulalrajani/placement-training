# Program to find biggest digit in it

number = int(input("Enter a number to find biggest digit in it : "))
tempNum = number
biggest = 0
while number != 0:
    remainder = number % 10
    number = number // 10
    if(remainder > biggest):
        biggest = remainder

print("The biggest number in ",tempNum," is : ",biggest)