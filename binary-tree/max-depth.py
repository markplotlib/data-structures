# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        >>> Solution().maxDepth(root=None)
        0
        >>> Solution().maxDepth(root=TreeNode(1))
        1
        >>> Solution().maxDepth(root=TreeNode(1,TreeNode(2)))
        2
        >>> Solution().maxDepth(TreeNode(3,TreeNode(9,None,None),TreeNode(20,TreeNode(15,None,None),TreeNode(7,None,None))))
        3
        """
        if root is None:
            return 0
        return 1 + max(Solution().maxDepth(root.left),
                       Solution().maxDepth(root.right))
