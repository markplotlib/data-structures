from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


if __name__ == '__main__':
    # construct linked list
    chain = LinkedList()

    # display length of uninitialized linked list (zero)
    print("Linked list length is " + str(chain.length))

