# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        set_nodes = set()
        while head:
            set_nodes.add(head)
            if head.next in set_nodes:
                return True
            head = head.next
        return False

    def hasCycleTwoPointer(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        slowPtr = head
        fastPtr = head.next
        while slowPtr != fastPtr:
            if not fastPtr or not fastPtr.next:
                return False
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        return True