
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prevNode = dummy
        dummy.next = head
        while head != None and head.next != None:
            n1 = head
            n2 = n1.next

            prevNode.next = n2
            n1.next = n2.next
            n2.next = n1

            head = n1.next
            prevNode = n1

        return dummy.next