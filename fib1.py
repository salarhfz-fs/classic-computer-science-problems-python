def fibonacci(n: int) -> int:
    if (n > 0 and n < 3): # base (non-recursive) case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(5))
    print(fibonacci(10))

