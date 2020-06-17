from node import Node

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if node is None else 1
