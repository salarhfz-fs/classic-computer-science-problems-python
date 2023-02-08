from typing import Dict
memo: Dict[int, int] = { 1: 1, 2: 1} # base cases

def fibonacci(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

if __name__ == '__main__':
    print(fibonacci(5))
    print(fibonacci(10))
    print(fibonacci(50))
    print(fibonacci(100))

