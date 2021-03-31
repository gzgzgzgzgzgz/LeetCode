# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 迭代
        # result_head = ListNode(0)
        # new_head = result_head
        # while l1 and l2:
        #     if l1.val > l2.val:
        #         new_head.next = l2
        #         new_head = new_head.next
        #         l2 = l2.next
        #     else:
        #         new_head.next = l1
        #         new_head = new_head.next
        #         l1 = l1.next
        # new_head.next = l1 if l1 else l2
        # return result_head.next
        # 递归
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next= self.mergeTwoLists(l1, l2.next)
            return l2
        