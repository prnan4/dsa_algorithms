# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
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
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        original = head
        slow = head
        fast = head
        
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
        reverse = self.reverseList(slow)

        while (original is not None) and (reverse is not None):
            if original.val != reverse.val:
                return False
            original = original.next
            reverse = reverse.next
        return True