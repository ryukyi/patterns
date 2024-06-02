"""
What are generator expressions in Python, and how do they differ from list comprehensions?
Could you write a generator expression that yields the squares of numbers from 1 to 10?
"""

# Generator expressions in Python are syntactically the same as list comprehensions except they use brackets "(" instead of square brackets "["
# Generator expressions create an object which implements the Iterator Protocol i.e __iter__ and __next__ methods and also yields results lazily.
# Unlike lists, generators compute and return values one at a time, streaming values hence using less memory than a list where all are loaded into memory.

if __name__ == "__main__":
    squares = (x**2 for x in range(1, 11))
    for i in squares:
        print(i)

"""
How do generators work in Python, and what are the benefits of using them over regular functions? 
Please write a generator function that yields the Fibonacci sequence up to a given number n.
"""

# Generators are iterables and use the yield keyword. Under the hood this yield keyword prompts the interpreter to create __iter__ and __next__ methods
# and enables output values to be computed and returned only when required.
# The benefit is efficient memory usage compared to a regular function where the entire output is loaded into memory.


def fibonacci(n):
    def fib_helper(n):
        a, b = 0, 1
        while a <= n:
            yield a
            a, b = b, a + b

    for num in fib_helper(n):
        yield num


if __name__ == "__main__":
    print(fibonacci(10))
