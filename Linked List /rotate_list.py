# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if (k == 0) or (head is None) or (head.next is None):
            return head
        
        temp = head     
        length = 1
        while temp.next is not None:
            temp = temp.next
            length += 1
        temp.next = head
        
        k = k % length
        i = length - k
        prev = None
        while i != 0:
            prev = head
            head = head.next
            i -= 1
        
        prev.next = None
        return head
    """
     Time Limit exceeded
    """
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if (k == 0) or (head is None) or (head.next is None):
            return head
        
        temp = head
        reverse = head
        
        while k != 0:
            if temp.next is None:
                temp = head
            else:
                temp = temp.next
            k -= 1
        
        prev = None
        
        if temp == head:
            return head
        
        while temp is not None:
            prev = reverse
            reverse = reverse.next
            temp = temp.next
        
        prev.next = None
        
        temp1 = reverse
        while temp1.next is not None:
            temp1 = temp1.next
        temp1.next = head
        return reverse
        
        
        
            