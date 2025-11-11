## Yield ##
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
var1 = gen1()
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))

def gen2():
    num1 = 0
    while True:
        temp = num1
        num1 += 2
        yield temp
var2 = gen2()
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))
print(next(var2))


def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        temp = num1
        num1 = num1 + num2
        num2 = temp
        yield temp
fib = fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
