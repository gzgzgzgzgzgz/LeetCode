# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        result_head = head
        prev = head
        head = head.next
        while head:
            if head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return result_head
            