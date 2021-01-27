# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# example
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])

# example
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = []
        cur = head
        while cur.next != None:
            arr.append(cur)
            cur = cur.next
        arr.append(cur)
        return arr[len(arr) // 2]


if __name__ == '__main__':
	f = ListNode(val=6)
	e = ListNode(val=5)
	d = ListNode(val=4, next=e)
	c = ListNode(val=3, next=d)
	b = ListNode(val=2, next=c)
	a = ListNode(val=1, next=b)
    # middleNode(a)
    # _ = input("paused")
	# e = ListNode(val=5, next=f)
    # middleNode(a)
