# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午5:21

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# in-place, iteratively
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None:
			return l2
		if l2 is None:
			return l1
		result = ListNode(-1)
		cur = result
		while (l1 and l2):
			if l1.val <= l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			cur = cur.next
		if l1:
			cur.next = l1
		if l2:
			cur.next = l2
		return result.next

# iteratively
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		dummy = cur = ListNode(0)
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1.next = l1
			else:
				cur.next = l2
				l2.next = l2
			cur = cur.next
		cur.next = l1 or l2
		return dummy.next

# recursively
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if not l1 or not l2:
			return l1 or l2
		if l1.val < l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2