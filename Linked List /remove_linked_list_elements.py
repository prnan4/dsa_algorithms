class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head is not None and head.val == val:
            head = head.next
       
        if head is None:
            return head
        
        temp_head = head
        prev = temp_head
        temp_head = temp_head.next
        
        while temp_head != None:
            if temp_head.val == val:
                prev.next = temp_head.next
                temp_head = temp_head.next
            else:
                prev = prev.next 
                temp_head = temp_head.next
                
        return head