# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        int_set = set()
        cur = head

        while cur.next is not None:
            if cur.val not in int_set:
                int_set.add(cur.val)
            # advance to next node
            cur = cur.next
        # finished product: full, ordered set

        # cast set to list
        list_int = list(int_set)

        # pop the value of the final tail, whose node gets next=None
        tail = ListNode(val=list_int.pop(), next=None)
        cur = tail
        prev = None

        while len(list_int) > 0:
            prev = ListNode(
                            val=list_int.pop(),
                            next=cur)
            cur = prev
            # note: pop() decrements list length, so terminal condition will be met

        return cur


if __name__ == '__main__':
	c = ListNode(val=2)
	b = ListNode(val=1, next=c)
	a = ListNode(val=1, next=b)

    # soln = Solution()
    # no_dupes = soln.deleteDuplicates(a)
