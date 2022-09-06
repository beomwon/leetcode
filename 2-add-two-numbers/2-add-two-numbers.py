# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        cur = answer
        carry = 0
        
        while True:
            if l1 == l2 == None and not carry:
                return answer.next
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            colsum = l1Val + l2Val + carry
            carry = colsum // 10
            newNode = ListNode(colsum % 10)
            cur.next = newNode
            cur = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            
        
    