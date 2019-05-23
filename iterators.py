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


class SimpleFizzBuzzIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        if not self.i % 3:
            return 'Fizz'
        elif not self.i % 5:
            return 'Buzz'
        else:
            return self.i


class ExtendedFizzBuzzIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.data = {3: 'Ala', 5: 'ma', 7: 'kota'}

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        for k, v in self.data.items():
            if not self.i % k:
                return v
        return self.i


print([a for a in IncrementIterator(10)])
print([a for a in SumIterator(10)])
print([a for a in PowIterator(10)])
print([a for a in FibIterator(10)])
print([a for a in SimpleFizzBuzzIterator(10)])
print([a for a in ExtendedFizzBuzzIterator(10)])
