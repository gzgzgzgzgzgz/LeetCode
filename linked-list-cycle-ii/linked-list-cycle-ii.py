# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        #关键是相遇后 新的头指针和慢指针相遇时的节点为开口
        slow_pointer, fast_pointer = head, head
        while (fast_pointer):
            slow_pointer = slow_pointer.next
            if fast_pointer.next:
                fast_pointer = fast_pointer.next.next
            else:
                return None
            if slow_pointer == fast_pointer:
                new_pointer = head
                while new_pointer != slow_pointer:
                    new_pointer = new_pointer.next
                    slow_pointer = slow_pointer.next
                return slow_pointer
        return None
            
        