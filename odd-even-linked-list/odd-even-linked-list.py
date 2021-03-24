# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None: return head
        #挑出两个ll 然后combine
        oddHead = head
        even = head.next
        evenHead = head.next
        while (evenHead and evenHead.next):
            oddHead.next = evenHead.next
            oddHead = evenHead.next
            evenHead.next = oddHead.next
            evenHead = oddHead.next
        oddHead.next = even
        return head
        