# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_node = ListNode(0, head)
        prev = dummy_node
        while (head):
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next
        return dummy_node.next