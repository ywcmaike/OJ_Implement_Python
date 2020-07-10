# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午4:08

# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# idea
# 使用快慢指针

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		slow = fast = self
		self.next = head
		while fast.next:
			if n:
				n -= 1
			else:
				slow = slow.next
			fast = fast.next
		slow.next = slow.next.next
		return self.next

# one pass
class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		self.next, nodelist = head, [self]
		while head.next:
			if len(nodelist) == n:
				nodelist.pop(0)
			nodelist += head,
			head = head.next
		nodelist[0].next = nodelist[0].next.next
		return self.next


