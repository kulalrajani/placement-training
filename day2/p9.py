num_of_requests = int(input("Enter numbr of requests : "))
array = list(map(int,input().split()))
sum = 0

for i in range(0,num_of_requests):
    if i % 2 == 0:
        sum += array[i]

if(sum < 0):
    print("Memory allocated by server1 is ",sum," memory units")
else:
    print("Memory dellocated by server1 is ",sum," memory units")
