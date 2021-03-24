# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_node = ListNode(0, head)
        slow_pointer = dummy_node
        fast_pointer = head
        for i in range(n):
            fast_pointer = fast_pointer.next
        while fast_pointer:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        slow_pointer.next = slow_pointer.next.next
        return dummy_node.next