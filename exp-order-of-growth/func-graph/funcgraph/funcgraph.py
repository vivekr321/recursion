from graphviz import *
from funcgraph.caller import *

dot = Digraph(comment='OrderOfGrowth')

def addnode(dot, str):
    dot.node(str)

def addedge(dot, frommode, tonode):
    dot.edge(frommode, tonode)

def printwithspace(spacecout, str):
    string = ""
    for index in range(0,spacecout):
        string = string + "----"
    print(string + str)

g_count = 0

func_dict = {}
def get_function_prefix(funcstr, level, callee = False):
    if func_dict.get(level) is None:
        func_dict[level] = {}
    if func_dict.get(level).get(funcstr) is None:
        func_dict.get(level)[funcstr] = 1
    else:
        if callee:
            func_dict.get(level)[funcstr] = func_dict.get(level)[funcstr] + 1

    return str(level) + "." + str(func_dict.get(level).get(funcstr)) + "." + funcstr

def drawtree(func):
    def inner(*args, **kwargs):
        global g_count
        g_count = g_count + 1
        caller = caller_name()
        callee = str(func.__name__) + str(list(args))

        # addedge(dot, str(g_count) + "." + caller, str(g_count+1) + "." + callee)
        addedge(dot, get_function_prefix(caller, g_count - 1), get_function_prefix(callee, g_count, True))
        retval = func(*args, **kwargs)
        g_count = g_count - 1
        return retval

    return inner

