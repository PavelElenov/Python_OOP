class reverse_iter:
    def __init__(self, values):
        self.values = list(reversed(list(values)))
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.values):
            raise StopIteration
        element_to_return = self.values[self.idx]
        self.idx += 1
        return element_to_return



