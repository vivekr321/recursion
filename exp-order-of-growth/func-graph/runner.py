from funcgraph.funcgraph import *

@drawtree
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


@drawtree
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(fib(8))
    print(dot.source)
    print(func_dict)

main()


