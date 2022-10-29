class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        with open('./result.txt', 'a') as file:
            file.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")
            file.close()

        # print(f"Function '{self.func.__name__}' was called. Result: {result}")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)


def read_file(path):
    with open(path) as file:
        print(file.read())
        file.close()


read_file('./result.txt')
