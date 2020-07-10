# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/10 下午7:25

# Given a linked list, determine if it has a cycle in it.
#
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
#
#
# Example 1:
#
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
#
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
#
# Example 3:
#
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
#
#
#
# Follow up:
#
# Can you solve it using O(1) (i.e. constant) memory?


# idea
# 快慢指针, 快追慢, 快2,

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		if head is None:
			return False
		fast = head.next
		while head is not None and fast is not None and fast.next is not None:
			if fast == head:
				return True
			else:
				fast = fast.next.next
				head = head.next
		return False

