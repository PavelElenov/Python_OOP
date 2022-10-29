class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'o', 'i', 'u', 'y']
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.string):
            element_to_return = self.string[self.idx]
            self.idx += 1
            if element_to_return.lower() in self.vowels:
                return element_to_return
            else:
                continue
        raise StopIteration



