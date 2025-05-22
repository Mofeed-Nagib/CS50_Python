class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity
        self._count = 0

    def __str__(self):
        return "🍪" * self._count

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self._count + n > self._capacity:
            raise ValueError("Too many cookies to deposit")
        self._count += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        if self._count - n < 0:
            raise ValueError("Too many cookies to withdraw")
        self._count -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._count