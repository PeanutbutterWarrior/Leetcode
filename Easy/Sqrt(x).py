def square_root(self, x: int) -> int:
    for i in range(x + 2):
        if i * i > x:
            return i - 1
    return 0
