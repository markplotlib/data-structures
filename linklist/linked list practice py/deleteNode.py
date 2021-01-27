https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # get the value of the next node
        # and assign it to this target node
        node.val = node.next.val
        # then chain this node to skip the next node
        # (which has the same redundant value of this node)
        node.next = node.next.next
