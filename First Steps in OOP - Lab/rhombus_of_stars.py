def get_line(n, i):
    spaces = n - 1 - i
    char = n - spaces
    print(" " * spaces + "* " * char)


def create_rhombus(n):
    for i in range(n):
        get_line(n, i)
    for j in range(n - 2, -1, -1):
        get_line(n, j)


n = int(input())
create_rhombus(n)
