class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.dictionary):
            raise StopIteration
        value_to_return = self.dictionary[self.idx]
        self.idx += 1
        return value_to_return


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

