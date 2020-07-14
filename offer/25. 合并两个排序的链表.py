# author: weicai ye
# email: yeweicai@zju.edu.cn 
# datetime: 2020/7/13 下午5:56


# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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

if __name__ == "__main__":
	pass