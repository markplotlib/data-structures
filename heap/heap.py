class Heap(object):
    """
    author: Kevin Lundeen, Seattle University
    Min heap. Elements are key:weight pairs.
    Operations are:
    1. construct from set of key:weight pairs (a dict), Θ(n)
    2. enqueue a new or existing key with its current weight, Θ(log n) worst case
    3. dequeue the key with the minimum weight, Θ(log n)
    4. empty tells if the heap is empty, Θ(1)

    >>> h = Heap({'a':1, 'b':10, 'c':-3})
    >>> (h.empty(), h.dequeue(), h.dequeue(), h.dequeue(), h.empty())
    (False, ('c', -3), ('a', 1), ('b', 10), True)

    >>> h = Heap({'a':1, 'b':10, 'c':-3})
    >>> h.enqueue('d', 99); h.enqueue('a', 101); h.enqueue('b', -10)
    >>> h.dequeue()
    ('b', -10)
    >>> h.enqueue('d', -1000); h.enqueue('c', 1000)
    >>> (h.empty(), h.dequeue(), h.dequeue(), h.dequeue(), h.empty())
    (False, ('d', -1000), ('a', 101), ('c', 1000), True)
    """

    def __init__(self, initial=None):
        """Construct a heap from the given initial list, Θ(n) time."""
        self.weights = {}  # the weight for a given key
        self.place = {}  # the index into heap where the key currently is placed
        self.heap = []  # the heap array
        if initial is not None:
            last = 0
            for key in initial:
                self.heap.append(key)
                self.weights[key] = initial[key]
                self.place[key] = last
                last += 1
            # print(self.weights)
            # print(self.place)
            # print(self.heap)
            self._heap_construct()

    def empty(self):
        """True if no more items in the heap."""
        return len(self.heap) == 0

    def enqueue(self, key, weight):
        """Put key into heap with given weight. If key is already present, this will change the weight and repair
        the heap as necessary.
        """
        if key in self.weights:
            old_w = self.weights[key]
            i = self.place[key]
        else:
            self.heap.append(key)
            old_w = None
            i = self._last()
            self.place[key] = i
        self.weights[key] = weight
        if old_w is None or old_w > weight:
            self._swap_up(i)
        elif old_w < weight:
            self._swap_down(i)

    def dequeue(self):
        """Remove minimum element and return its key and weight."""
        last = self._last()
        if last < 0:
            return None

        # retrieve the minimum element (at the root)
        key = self.heap[0]
        weight = self.weights[key]
        del (self.weights[key])
        del (self.place[key])

        # remove the last element and place it at the root, then fix the heap
        if last > 0:
            self.heap[0] = self.heap.pop()
            self.place[self.heap[0]] = 0
            self._swap_down(0)
        else:
            del (self.heap[0])

        return key, weight

    def _heap_construct(self):
        """Turn self.heap into a heap."""
        last_parent = self._parent(self._last())
        for i in range(last_parent, -1, -1):
            self._swap_down(i)

    def _weight(self, i):
        if i > self._last():
            return None
        return self.weights[self.heap[i]]

    def _last(self):
        return len(self.heap) - 1

    def _parent(self, i):
        return (i - 1) >> 1  # bit-wise for (i-1) // 2

    def _children(self, p):
        left = (p << 1) + 1  # bit-wise for 2*p + 1
        right = left + 1
        return (left, right)

    def _swap_up(self, i):
        while i > 0:
            p = self._parent(i)
            if self._weight(i) < self._weight(p):
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                self.place[self.heap[i]] = i
                self.place[self.heap[p]] = p
                # self._swap_up(p)
                i = p
            else:
                return

    def _swap_down(self, p):
        child, right = self._children(p)
        child_w = self._weight(child)
        if child_w is None:
            return
        right_w = self._weight(right)
        if right_w is not None and right_w < child_w:
            child = right
            child_w = right_w
        if self._weight(p) > child_w:
            self.heap[child], self.heap[p] = self.heap[p], self.heap[child]
            self.place[self.heap[child]] = child
            self.place[self.heap[p]] = p
            self._swap_down(child)

