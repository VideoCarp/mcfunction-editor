def switch(expr, conditions):
    for k, v in conditions.items():
        if expr == k:
            v()


def match_iterable(iterable, conditions):
    for value in iterable:
        for k, v in conditions.items():
            if value == k:
                v()


def match_with(expr, conditions, multiexpr):
    for k, v in conditions.items():
        if expr == k:
            if type(v) == tuple:
                if v[0] == True:
                    v[1]()
                elif multiexpr:
                    for eachlambda in v:
                        eachlambda()
            else:
                v()


def match_with_iter(iterable, conditions, multiexpr = False):
    for value in iterable:
        match_with(value, conditions, multiexpr)


def typename(value):
    result = ""
    valuetype = type(value)
    result += str(valuetype)[str(valuetype).find("'") + 1:]
    result = result[:result.find("'")]
    return result

def repeat(value, amount):
    result = [value]
    for _ in range(amount):
        result.append(value)
    return result


def dyn_join(lst, delimiter = ""):
    result = ""
    for v in lst:
        result += str(v)
        result += delimiter
    return result


def read(path):
    with open(path) as f:
        return f.read()


def write(path, contents, mode = "+w"):
    with open(path, mode) as f:
        f.write(contents)

def cmu_do(args):
    rules = {
        "&red": "\u001b[31m",
        "&reset": "\u001b[0m",
        "&black": "\u001b[30m",
        "&lime": "\u001b[32m",
        "&blue": "\u001b[34m",
        "&magenta": "\u001b[35m",
        "&cyan": "\u001b[36m",
        "&yellow": "\u001b[33m",
        "&white": "\u001b[0m",
        "&bold": "\u001b[1m",
        "&underline": "\u001b[4m",
        "&reverse": "\u001b[7m"
    }
    for k, v in rules.items():
        args = args.replace(k, v)
    return args
