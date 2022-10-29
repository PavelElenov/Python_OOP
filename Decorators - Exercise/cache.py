def cache(func):
    data = {}

    def wrapper(n):
        if n in data:
            return data[n]
        result = func(n)
        data[n] = result
        return result

    wrapper.log = data
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))

