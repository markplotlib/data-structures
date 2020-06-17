class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if node is None else 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
