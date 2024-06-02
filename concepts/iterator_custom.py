"""
Can you explain how to create a custom iterator in Python?
Please provide an example implementation of a custom iterator class that iterates over the first n even numbers.
"""


# An iterator is an object which implements __iter__ and __next__(). This is called the iterator protocol.
# Every iterator is also an iterable because it implements the __iter__() method.
# Not every iterable is an iterator. For example, a list and set are iterable but not iterators.
class ExampleIter:
    def __init__(self, low, high, step: int = 1):
        self.current = low - step
        self.high = high
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.high:
            return self.current
        raise StopIteration


if __name__ == "__main__":
    iterator = ExampleIter(-33, 10, 2)
    for i in iterator:
        print(i)
