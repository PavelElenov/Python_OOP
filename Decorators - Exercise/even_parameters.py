def even_parameters(func):
    def wrapper(*args):
        result = 0
        even = True
        for v in args:
            if isinstance(v, int):
                if v % 2 != 0:
                    even = False
                    break
            else:
                even = False
                break
        if even:
            result = func(*args)
            return result
        else:
            return "Please use only even numbers!"

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


