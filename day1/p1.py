#Program to check if an integer is a perfect square

inputNum = int(input("Enter a number to check if it is a perfect square : "))
rootNum = int(inputNum ** 0.5)
if rootNum * rootNum == inputNum:
    print(inputNum," is a perfect square number")
else:
    print(inputNum," is not a perfect square number")