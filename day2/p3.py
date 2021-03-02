#Program to find sum of n + n^2 + n^3 + ...

n = int(input("Enter a base value : "))
m = int(input("Enter the power value : "))
sum = 0 

for i in range(1,m+1):
    sum += n ** i

print("The of the series is : ",sum)
