def peasantMultiply(x, y):
    if x == 0:
        return 0
    x_prime = x // 2
    y_prime = y + y
    prod = peasantMultiply(x_prime, y_prime)
    if x % 2 == 1:
        prod += y
    return prod


peasantMultiply(2, 3)