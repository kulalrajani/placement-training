#Program to check if the brackets are placed correctly

brackets = input("Enter the string of brackets : ")
stack = []
flag = True

for bracket in brackets:
    if bracket == '{' or bracket == '(' or bracket == '[':
        stack.append(bracket)
        continue
    elif bracket == ']' and stack.pop() != '[':
        flag =False
        break
    elif bracket == ')' and stack.pop() != '(':
        flag =False
        break
    elif bracket == '}' and stack.pop() != '{':
        flag =False
        break

if(flag) and len(stack) == 0:
    print("Valid")
else:
    print("Invalid")