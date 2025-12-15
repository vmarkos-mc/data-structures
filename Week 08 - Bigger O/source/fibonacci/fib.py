def fib(n):
    result = 0
    f = [n]
    while f:
        current = f.pop()
        if current in [0, 1]:
            result += current
        else:
            f += [current - 1, current - 2]
    return result

if __name__ == "__main__":
    print([fib(x) for x in range(100)])