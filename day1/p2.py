# Find smallest digit in a integer number

number = int(input("Enter a number to find smallest digit in it : "))
tempNum = number
small = None
while number != 0:
    remainder = number % 10
    number = number // 10
    if(small == None or remainder < small):
        small = remainder

print("The smallest number in ",tempNum," is : ",small)