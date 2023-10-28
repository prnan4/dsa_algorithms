# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def merge(n1, n2):
            dummy = ListNode(-1)
            prev = dummy 

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

        def mergesort(head):

            if (not head) or (not head.next):
                return head
            
            else:

                slow = head
                fast = head
                
                while fast and fast.next:
                    prev = slow
                    fast = fast.next.next
                    slow = slow.next
                    
                prev.next = None

                merged_left = mergesort(head)
                merged_right = mergesort(slow)

                result = merge(merged_left, merged_right)
                return result

        return mergesort(head)




        


            
        


        