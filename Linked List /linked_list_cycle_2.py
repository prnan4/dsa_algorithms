# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        start = head
        fast = head
        
        first = True
        while (slow != fast) or first:
            first = False
            if (fast is None) or (fast.next is None):
                return None
            slow = slow.next
            fast = fast.next.next
            
        while slow != start:
            slow = slow.next
            start = start.next
        return start
        
        
        