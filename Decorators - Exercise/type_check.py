def type_check(type):
    def decorator(func):
        def wrapper(*args):
            if isinstance(*args, type):
                result = func(*args)
                return result
            return 'Bad Type'

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
