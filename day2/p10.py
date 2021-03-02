#Count of perfect squares in the array

num_of_requests = int(input("Enter numbr of requests : "))
array = list(map(int,input().split()))[:num_of_requests]
count = 0

for num in array:
    n = int(num ** 0.5)
    if n * n == num:
        count += 1
      
print("Count of perfect squares in the array : ",count)