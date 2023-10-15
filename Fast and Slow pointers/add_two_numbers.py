# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # ========================== APPROACH 1 ==========================
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l3 = None
        carry = 0
        
        while (l1 or l2):
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
                
            l3_val = l1_val + l2_val + carry
            
            if l3_val > 9:
                l3_val = l3_val % 10
                carry = 1
            else:
                carry = 0
            
            if l3 is not None:
                temp = ListNode(l3_val, l3.next)
                l3.next = temp
                l3 = l3.next
            else:
                temp = ListNode(l3_val, l3)
                l3 = temp
                l4 = l3

        if carry == 1:
            temp = ListNode(1, l3.next)
            l3.next = temp
        return l4

    # ========================== APPROACH 2 ==========================
    # Optimised for time
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while (l1) or (l2) or (carry != 0) :
            
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
                
            l3_val = l1_val + l2_val + carry
            carry = l3_val // 10
            
            temp = ListNode(l3_val % 10)
            curr.next = temp
            curr = temp
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            
    # October 14       
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        resNode = None
        while (l1 is not None) or (l2 is not None):
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0 

            sum_num = a + b + carry
            if sum_num >= 10:
                sum_num %= 10
                carry = 1
            else:
                carry = 0
            
            newNode = ListNode(sum_num, None)
            if resNode:
                resNode.next = newNode
            else:
                head = newNode
            resNode = newNode
            
            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        if carry == 1:
            newNode = ListNode(carry, None)
            resNode.next = newNode
        return head
        