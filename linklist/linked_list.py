from node import Node

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if node is None else 1

    def add(self, new_num):
        if self.head is None:
            self.head = Node(new_num)
        node_n = self.head
        while node_n is not None:
            node_n = node_n.next
        node_n = Node(new_num)
        self.length += 1


if __name__ == '__main__':
    # construct linked list
    chain0 = LinkedList()

    # display length of uninitialized linked list (zero)
    print("Empty chain has length of " + str(chain0.length))

    # initialize linked list
    n3 = Node(3)
    chain1 = LinkedList(n3)
    print("single link chain has length of " + str(chain1.length))
    print("value stored is", chain1.head.data)

    print("Adding 2 links to original chain.")
    chain0.add(2); chain0.add(1)
    print("New length of that chain is", chain0.length)
