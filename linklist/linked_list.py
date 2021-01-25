class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def to_string(self):
        if self.head is None:
            return ""
        node_n = self.head
        to_str = ""
        while node_n is not None:
            import pdb; pdb.set_trace()
            to_str = " ".join([to_str, str(node_n.data)])
            node_n = node_n.next
        return to_str.strip()


if __name__ == '__main__':
    # construct linked list
    chain0 = LinkedList()

    # display length of uninitialized linked list (zero)
    print("Empty chain has length of " + str(chain0.length))
    print("contents: \"", chain0.to_string(), "\"\n", sep="")

    # initialize linked list
    n3 = Node(3)
    chain1 = LinkedList(n3)
    print("single link chain has length of " + str(chain1.length))
    print("value stored is", chain1.head.data)
    print("contents: \"", chain1.to_string(), "\"\n", sep="")

    print("Adding 2 links to original chain.")
    chain0.add(2); chain0.add(1)
    print("New length of that chain is", chain0.length)
    print("contents: \"", chain0.to_string(), "\"\n", sep="")
