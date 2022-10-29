def possible_permutations(numbers):
    for num in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num != num2 and num != num3 and num2 != num3:
                    yield [num, num2, num3]


[print(n) for n in possible_permutations([1, 2, 3])]