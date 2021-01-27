https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
# def deleteDuplicates(self, head: ListNode) -> ListNode:
def deleteDuplicates(head: ListNode) -> ListNode:
	if head == None:
		return None

	n = head

	while n.next is not None:
		if n.val == n.next.val:
			n.next = n.next.next
		n = n.next

	return head


if __name__ == '__main__':
	c = ListNode(val=2)
	b = ListNode(val=1, next=c)
	a = ListNode(val=1, next=b)
	deleteDuplicates(a)
