#Program to print n-th fibo term

n = int(input("Enter a number : "))

if n == 1:
    print("The ",n,"th fibo number is : ",1)
elif n == 2:
    print("The ",n,"th fibo number is : ",2)
else:
    f1 = 1
    f2 = 2
    count = 2
    while count < n:
        f3 = f1 + f2
        f1 = f2
        f2= f3
        count += 1

    print("The ",n,"th fibo number is : ",f3)
