# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next == None: return True
        #先找到中点->快慢指针 然后翻转后半部分 然后compare
        fast_pointer, slow_pointer = head, head
        while (fast_pointer.next and fast_pointer.next.next):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
        head_second_half = slow_pointer.next
        prev = slow_pointer
        while (head_second_half):
            temp_next = head_second_half.next
            head_second_half.next = prev
            prev = head_second_half
            head_second_half = temp_next
            
        while (prev != slow_pointer):
            if prev.val != head.val:
                return False
            head = head.next
            prev = prev.next
        return True
        
        