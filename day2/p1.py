#Program to find n-th prime number
import os
n = int(input("Enter a number : "))

if n == 1:
    print("2")
    exit()

count = 1
i = 3

while count < n:
    flag = True
    for j in range(2,(i//2)+1):
        if i % j == 0:
            flag = False
            break
    
    if flag == True:
        count += 1

    i += 1

print("The",n,"th prime number is : ",i-1)
