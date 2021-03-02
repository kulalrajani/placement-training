#Program to print the n-th term in the series of 2 1 3 2 5 3 7 5 11 8 13 13 17 21
def printFibo(n):
    f1 = 1
    f2 = 2
    if n == 1:
        return f1
    elif n == 2:
        return f2
    else:
        for i in range(3,n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

def printPrime(n):
    if n == 1:
        return 2
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
    return i-1

n = int(input("Enter a number : "))
if n % 2 == 0:
    print(printFibo(n//2))
else:
    print(printPrime(n//2+1))