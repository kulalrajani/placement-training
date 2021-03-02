# n = int(input("Enter number of pair of shoes : "))
# p = int(input("Enter maximum pair of shoes that purchaser can buy"))

total_and_max = input().split(" ")
n = int(total_and_max[0])
p = int(total_and_max[1])

array = []

for i in range(n):
    array.append(int(input()))

print(array)