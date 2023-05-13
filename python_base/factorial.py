def fact(inputNum):
    res = 1
    while (inputNum > 1):
        res *= inputNum
        inputNum -= 1
    return res

x =int(input('insert number: '))
print(fact(x))
