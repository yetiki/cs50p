"""Suppose that you'd like to implement a cookie jar in which to store
cookies. This program implements a class called Jar with the following
methods:

__init__ : to initialize a cookie jar with the given capacity, which
represents the maximum number of cookies that can fit in the cookie jar. If
capacity is not a non-negative int, though, __init__ instead raises a
ValueError.

__str__: to return a str with n 🍪, where n is the number of cookies in the
cookie jar. For instance, if there are 3 cookies in the cookie jar, then str
should return "🍪🍪🍪"

deposit: to add n cookies to the cookie jar. If adding that many would
exceed the cookie jar's capacity, though, deposit instead raises a
ValueError.

withdraw: to remove n cookies from the cookie jar. Nom nom nom. If there
aren't that many cookies in the cookie jar, though, withdraw instead raises
a ValueError.

capacity: to return the cookie jar's capacity.

size: to return the number of cookies actually in the cookie jar, initially
0.
"""

class Jar:
    def __init__(self, capacity: int = 12) -> None:
        self.capacity = capacity
        self.size = 0

    def __repr__(self) -> str:
        return f"Jar(capacity={self.capacity}, size={self.size})"

    def __str__(self) -> str:
        return "🍪" * self.size

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError(f"Unsupported value: {capacity}. 'capacity' must be a positive integer.")

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if isinstance(size, int) and 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError(f"Unsupported value: {size}. 'size' must be a non-negative integer, and not exceed 'capacity'.")

    def deposit(self, n: int) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Unsupported value: {n}. 'n' must be a non-negative integer.")
        if self.size + n > self.capacity:
            raise ValueError(f"Unsupported value: {n}. 'size' + 'n' would exceed jar 'capacity'.")
        self.size += n

    def withdraw(self, n: int) -> None:
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Unsupported value: {n}. 'n' must be a non-negative integer.")
        if self.size - n < 0:
            raise ValueError(f"Unsupported value: {n}. 'size' - 'n' would be negative.")
        self.size -= n