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
        curr = None
        temp = head
        while temp:
            prev = temp.next
            temp.next = curr
            curr = temp
            temp = prev
        return curr
        