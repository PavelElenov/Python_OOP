class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        value_to_return = self.value
        self.value += self.step
        self.count -= 1
        return value_to_return



