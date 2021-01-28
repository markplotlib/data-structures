# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # yes
        if p is None and q is None:
            return True

        # fail cases
        # only 1 null
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        # root-only, diff values
        if p.val != q.val:
            return False

        return isSameTree(self, p.left, q.left) and isSameTree(self, p.right, q.right)

if __name__ == '__main__':
    c = TreeNode(3, None, None)
    f = TreeNode(3, None, None)
    b = TreeNode(2, None, None)
    e = TreeNode(2, None, None)
    a = TreeNode(1, b, c)
    d = TreeNode(1, e, f)

    soln = Solution()
    expected_true = soln.isSameTree(p=a, q=b)
    print(expected_true)

    # _ = input('paused...')
    # y = TreeNode(2, None, None)
    # z = TreeNode(2, None, None)
    # w = TreeNode(1, y, None)
    # x = TreeNode(1, None, z)
    # expected_false = soln.isSameTree(p=a, q=b)
    # print(expected_false)
