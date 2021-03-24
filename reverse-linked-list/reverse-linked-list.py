# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #递归
        # if not head or not head.next:
        #     return head
        # cur = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return cur
        
        #iteration
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
        