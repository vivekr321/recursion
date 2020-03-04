from funcgraph.funcgraph import *
from recursion_types.fib import *
from recursion_types.even_odd import *

@drawtree
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    # factorial(5)

    val = even(5)

    print(dot.source)
    print(func_dict)


main()


