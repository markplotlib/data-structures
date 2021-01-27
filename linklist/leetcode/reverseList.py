https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # init
        cur = head
        prev = None
        
        # terminal case: cur==None (on last iteration)
        while cur is not None:
            
            # reversal of linked list direction
            cur.next = prev
            
            # advance prev, for next iteration
            prev = cur
            
            # advance to next node
            cur = cur.next    
        
        return prev  # cur==None
