# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        # Step 1: check if k nodes exist
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count < k:
            return head
        
        # Step 2: reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: connect with next part
        head.next = self.reverseKGroup(curr, k)
        
        return prev
      
        