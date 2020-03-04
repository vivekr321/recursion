from funcgraph.funcgraph import *

@drawtree
def odd(n):
    if n == 0:
        return False
    else:
        return even(n-1)

@drawtree
def even(n):
    if n == 0:
        return True
    else:
        return odd(n-1)