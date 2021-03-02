#Program to find sum of 1 - n + n^2 - n^3 + ...

n = int(input("Enter a base value : "))
m = int(input("Enter the power value : "))
sum = 1

for i in range(1,m+1):
    if i % 2 == 0:
        sum += n ** i
    else:
        sum -= n ** i

print("sum of the series is: ",sum)
