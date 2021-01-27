# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # init
        cur = head
        prev = None

        # terminal case: cur==None (on last iteration)
        while cur is not None:

            # temp
            tmp = cur.next

            # reversal of linked list direction
            cur.next = prev

            # advance prev, for next iteration
            prev = cur

            # advance to next node
            cur = tmp

        return prev


if __name__ == '__main__':
	e = ListNode(val=5)
	d = ListNode(val=4, next=e)
	c = ListNode(val=3, next=d)
	b = ListNode(val=2, next=c)
	a = ListNode(val=1, next=b)

    # run in CLI
    # soln = Solution()
    # s1 = soln.reverseList(a)
    # print(s1)
