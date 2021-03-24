# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         dummy_node = ListNode(0,head)
#         temp = dummy_node
#         while (temp.next and temp.next.next):
#             node1 = temp.next
#             node2 = temp.next.next
            
#             node1.next = node2.next
#             node2.next = node1
#             temp.next = node2
            
#             temp = node1
#         return dummy_node.next
        #递归
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead
            
