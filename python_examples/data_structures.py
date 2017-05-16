"""
Coding examples for basic data structures.

    * arrays
    * stacks
    * queues
    * deques

"""
import ctypes


class DynamicArray(object):
    """DynamicArray() -> array

    **Python** implementation of an array, where existing
    capacity is doubled when new space is required.

    This demonstrates the advantages of amortization of costs
    over the life of a function.

    While the cost of doubling the array is expensive it is
    far less expensive than adding one cell over time.

    >>> d = data_structures.DynamicArray()
    >>> d.items
    0
    >>> d.capacity
    1
    >>> d.append('one')
    >>> d.items
    1
    >>> d.capacity
    1
    >>> d.append('two')
    >>> d.items
    2
    >>> d.capacity
    2
    >>> foo = [d.append(x) for x in range(16)]
    >>> d.items
    18
    >>> d.capacity
    32
    """

    def __init__(self):
        self.items = 0
        self.capacity = 1
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.items

    def __getitem__(self, key):
        """get(key) -> value"""
        if not 0 <= key < self.items:
            return IndexError('Key is out of bounds!')

        return self.array[key]

    def append(self, element):
        """append(value)"""
        if self.items == self.capacity:
            self._resize(2 * self.capacity)

        self.array[self.items] = element
        self.items += 1

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)

        for key in range(self.items):
            new_array[key] = self.array[key]

        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()


class ListStack(object):
    """ListStack() -> stack

    Implement a **stack** - Using python lists

    >>> q = data_structures.ListStack()
    >>> for i in range(5): q.push(i)
    >>> for i in range(5): print q.pop()
    4
    3
    2
    1
    0
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """is_empty() -> bool"""
        return self.items == []

    def push(self, item):
        """push(item)"""
        self.items.append(item)

    def pop(self):
        """pop() -> item"""
        return self.items.pop()

    def peek(self):
        """peek() -> item"""
        return self.items[len(self.items) - 1]

    def size(self):
        """size() -> int"""
        return len(self.items)


class Queue2Stacks(object):
    """Queue2Stacks() -> stack

    Implement a **queue** - Using two stacks (python lists)

    >>> q = data_structures.Queue2Stacks()
    >>> for i in range(5): q.push(i)
    >>> for i in range(5): print q.pop()
    0
    1
    2
    3
    4
    """

    def __init__(self):
        # Two Stacks
        self.input = []
        self.output = []

    def __del__(self):
        del self.input
        del self.output

    def push(self, element):
        """push(item)"""
        self.input.append(element)

    def pop(self):
        """pop() -> item"""
        while not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output.pop()


class ListQueue(object):
    """ListQueue() -> queue

    Implement a **queue** - Using python lists

    >>> q = data_structures.ListQueue()
    >>> for i in range(5): q.push(i)
    >>> for i in range(5): print q.pop()
    0
    1
    2
    3
    4
    """

    def __init__(self):
        self.items = []

    def __del__(self):
        del self.items

    def push(self, item):
        """push(item)"""
        self.items.append(item)

    def pop(self):
        """pop() -> item"""
        return self.items.pop(0)

    def is_empty(self):
        """is_empty() -> bool"""
        return self.items == []

    def size(self):
        """size() -> int"""
        return len(self.items)


class ListDeque(object):
    """ListDeque() -> deque

    Implement a **deque** - Using python lists.


    >>> q = data_structures.ListDeque()
    >>> q.is_empty()
    True
    >>> for i in range(4): q.push(i)
    >>> for i in range(4): q.lpush(i)
    >>> for i in range(2): print(q.lpop())
    3
    2
    >>> for i in range(5): print(q.pop())
    3
    2
    1
    0
    0
    """

    def __init__(self):
        self.items = []

    def __del__(self):
        del self.items

    def is_empty(self):
        """is_empty() -> bool"""
        return self.items == []

    def size(self):
        """size() -> int"""
        return len(self.items)

    def push(self, item):
        """push(item) -> bool Right"""
        self.items.append(item)

    def lpush(self, item):
        """lpush(item) -> bool Left"""
        self.items.insert(0, item)

    def pop(self):
        """pop() -> item Right"""
        return self.items.pop()

    def lpop(self):
        """lpop() -> item Left"""
        return self.items.pop(0)


if __name__ == "__main__":  # pragma: no cover
    pass
