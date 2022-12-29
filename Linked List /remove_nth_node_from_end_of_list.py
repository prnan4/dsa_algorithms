# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        l = head
        r = head
        
        while(n):
            r = r.next
            n -= 1
        
        while r is not None:
            r = r.next
            prev = l
            l = l.next
        
        if l == head:
            return head.next
        else:
            prev.next = l.next
            return head

    # 28 Dec 2022
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if head.next is None:
            return None
        
        prev = head
        later = head
        curr = head
        temp = head
        while n > 0:
            later = later.next
            n -= 1
            
        if later is None:
            return temp.next 
        
        while later:
            later = later.next 
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        return temp
        