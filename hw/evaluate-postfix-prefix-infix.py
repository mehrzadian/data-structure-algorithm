print(7 // 3)
kind = int(input("if postfix:-1, infix:0, prefix:1\n"))
str = input()


# evaluate if prefix or postfix

def postfixEvaluation(str):
    stack = []
    operators = {'+', '-', '*', '/'}
    for i in str:
        if i.isnumeric():
            stack.append(int(i))
        elif i in operators:
            operation(-1,i, stack)
        else:
            return "unacceptable value!"
    return stack.pop()


def operation(kind,i, stack):
    a = stack.pop()
    b = stack.pop()
    if kind==-1:
        match i:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '/':
                result = b // a
            case '*':
                result = a * b
            case '^':
                result = a ** b
    else:
        match i:
            case '+':
                result = a + b
            case '-':
                result = a - b
            case '/':
                result = a // b
            case '*':
                result = a * b
            case '^':
                result = a ** b
    stack.append(result)


def prefixEvaluation(str):
    stack = []
    operators = {'+', '-', '*', '/'}

    for i in str[::-1]:
        if i.isnumeric():
            stack.append(int(i))
        elif i in operators:
            operation(1,i, stack)
        else:
            return "unacceptable value!"
    return stack.pop()


if kind == -1:
    print(postfixEvaluation(str))
else:
    print(prefixEvaluation(str))
