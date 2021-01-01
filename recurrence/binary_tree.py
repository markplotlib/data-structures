# divide-and-conquer algorithm

def levels(tree):
    """Recursively computes the number of levels in a binary tree.
    input: binary tree as a 3-tuple (value, left, right), where empty children
    are represented as None
    output: number of levels in tree
    >>> levels(None)
    0
    >>> levels(('just the root', None, None))
    1
    >>> levels(('root', ('left1', None, None), ('right1', None, None)))
    2
    >>> levels(('root', ('left1', None, ('lr', ('lrr', None, None), None)),
    ('right1', ('rl', None, None), None)))
    4
    """
    if tree is None:
        return 0
    else:
        value, left, right = tree
        return 1 + max(levels(left), levels(right))


def preorder(tree):
    """Recursively prints each value in the tree in preorder traversal:
    root, left subtree, right subtree.
    input: binary tree as a 3-tuple (value, left, right), where empty children
    are represented as None
    output: console output of node values in preorder traversal
    """
    if tree is not None:
        value, left, right = tree
        print(value)
        preorder(left)
        preorder(right)
