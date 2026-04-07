# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
       
        # Step 1: Find length
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        # Step 2: If head needs to be removed
        if n == length:
            return head.next
        
        # Step 3: Go to (L - n - 1) node
        temp = head
        for _ in range(length - n - 1):
            temp = temp.next
        
        # Step 4: Delete node
        temp.next = temp.next.next
        
        return head