stack =[]
str = input()
operators = {"+", "-", "*", "/", "^"}
str = str[::-1]
for i in str:
    if i in operators:
        a=stack.pop()
        b= stack.pop()
        temp = a+b+i
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)
