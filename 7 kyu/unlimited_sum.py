def sum(*args):
    return reduce(lambda a, b: a + b, (c for c in args if isinstance(c, int)))


# def sum(*args):
#     return __builtins__.sum(filter(lambda a: isinstance(a, int), args))

assert sum(1, 2, 3) == 6
assert sum('1', 1, '2', 2) == 3
