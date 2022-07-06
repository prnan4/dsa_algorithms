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
        
        