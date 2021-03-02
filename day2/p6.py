#Program to print the number of brackets if they placed correctly

brackets = input("Enter the string of brackets : ")

oc = 0
cc = 0
flag = True

for ch in brackets:
    if ch == "{":
        oc += 1
    else:
        cc += 1
    if cc > oc:
        flag = False
        break

if flag and oc == cc:
    print("The number of pairs : ",oc)
else:
    print("Th brackets are not arranged properly")