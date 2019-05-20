from collections import OrderedDict, Counter


class IncrementIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        return self.i


class SumIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.current += self.i
        return self.current


class PowIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        return self.i * self.i


class FibIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a


print([a for a in IncrementIterator(20)])
print([a for a in SumIterator(20)])
print([a for a in PowIterator(20)])
print([a for a in FibIterator(20)])
