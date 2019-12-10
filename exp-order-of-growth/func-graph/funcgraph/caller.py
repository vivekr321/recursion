import inspect

def caller_name(skip_frames=2):

    stack = inspect.stack()
    start = 0 + skip_frames
    if len(stack) < start + 1:
      return ''
    parentframe = stack[start][0]

    name = []
    module = inspect.getmodule(parentframe)
    if module and module.__name__ != "__main__":
        name.append(module.__name__)
    # detect classname
    if 'self' in parentframe.f_locals:
        name.append(parentframe.f_locals['self'].__class__.__name__)
    codename = parentframe.f_code.co_name
    _local = inspect.getargvalues(parentframe)
    values = []
    for val in _local.locals.values():
        values.append(val)
    if codename != '<module>':  # top level usually
        name.append( codename + str(values) ) # function or a method

    del parentframe, stack

    return ".".join(name)