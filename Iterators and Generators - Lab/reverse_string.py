def reverse_text(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]


print(str(reverse_text("step")))
