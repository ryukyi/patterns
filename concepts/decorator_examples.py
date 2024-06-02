"""Describe how you can use decorators to cache the results of a function to improve performance"""

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    # adds 2 calls on the stack per run
    # 499 exceeds 1000 call stack limit recursion depth and fails
    print(fibonacci(498))
