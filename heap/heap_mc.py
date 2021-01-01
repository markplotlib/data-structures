class Heap:
    """
    Min heap. Elements are key:weight pairs.
    Operations:
    1. construct from set of key:weight pairs (a dict). This is Θ(n)
    """

    def __init__(self):
        self.weights = {}