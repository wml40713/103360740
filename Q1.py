from Stack import Stack

def infixToPrefix(infixexpr):
    prec = {}
    prec["*"] = 3  #3>2>1
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    opStack = Stack()
    prefixList = []
    temp = []
    tokenList = infixexpr.split()
    tokenList.reverse()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            temp = "".join(prefixList)
            temp = token + temp
            prefixList = list(temp)
        elif token == ')':
            opStack.push(token)
        elif token == '(':
            topToken = opStack.pop()
            while topToken != ')':
                temp = "".join(prefixList)
                temp = topToken + temp
                prefixList = list(temp)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  temp = "".join(prefixList)
                  temp = opStack.pop() + temp
                  prefixList = list(temp)
            opStack.push(token)

    while not opStack.isEmpty():
        temp = "".join(prefixList)
        temp = opStack.pop() + temp
        prefixList = list(temp)
    return " ".join(prefixList)

print (infixToPrefix("A + B"))
print(infixToPrefix("A * B + C * D"))
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )"))