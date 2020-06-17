from node import Node

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.length = 0 if node is None else 1


if __name__ == '__main__':
    # construct linked list
    chain0 = LinkedList()

    # display length of uninitialized linked list (zero)
    print("Empty chain has length of " + str(chain0.length))

    # initialize linked list
    print("New chain, containing sequence of digits of pi ...")
    n3 = Node(3)
    chain_pi = LinkedList(n3)
    print("Pi chain has length of " + str(chain_pi.length))
    print(chain_pi.head.data)
