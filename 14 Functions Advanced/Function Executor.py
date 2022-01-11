def func_executor(*args):
    results = []
    for function, data in args:
        results.append(function(*data))
    return results