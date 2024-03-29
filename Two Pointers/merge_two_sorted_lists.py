# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    # ========================== APPROACH 1 ==========================
    # Iterative
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        a = l1
        b = l2
        
        if (not a) and (not b):
            return None
        elif not a:
            return b
        elif not b:
            return a
        
        while l1 and l2:
            if l1.val <= l2.val:
                while (l1 is not None) and (l1.val <= l2.val):
                    prev = l1
                    l1 = l1.next
                prev.next = l2
            
            else:
                while (l2 is not None) and (l2.val <= l1.val):
                    prev = l2
                    l2 = l2.next
                prev.next = l1
            
        if a.val <= b.val:
            return a
        else:
            return b
            
    # ========================== APPROACH 2 ==========================
    # Recursive        
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            
    # October 18 2023
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(-1)
        prev = dummy 

        n1 = list1
        n2 = list2
        while n1 and n2:
            if n1.val < n2.val:
                prev.next = n1
                n1 = n1.next

            else:
                prev.next = n2
                n2 = n2.next

            prev = prev.next

        prev.next = n1 if n1 else n2
        return dummy.next
        