# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # Iterative approach
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = None
        temp = head
        while temp:
            prev = temp.next
            temp.next = curr
            curr = temp
            temp = prev
        return curr

    # Iterative approach 2  
    def reverseList(self, head):
        # List is empty
        if head is None:
            return head
        else:
            prev = head
            
        # Single node in list
        if prev.next is None:
            return prev
        else:
            curr = prev.next
         
        # Two nodes in list 
        if curr.next is None:
            curr.next = prev
            prev.next = None
            return curr
        
        else:
            later = curr.next 
            
        node1 = True
        
        while curr is not None:
            curr.next = prev
            if node1 is True:
                prev.next = None
                node1 = False
            prev = curr
            curr = later 
            if later is not None:
                later = later.next
        return prev
    # Recursive approach
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp
        
        