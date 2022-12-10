"""
https://leetcode.com/problems/add-two-numbers
Approach :-
Iterate through both linkedlists and form the number.
Add the numbers and insert it into the result linkedlist
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        y = 0
        temp=1
        while l1!=None:
            x=x+l1.val*temp
            temp*=10
            l1 = l1.next
        temp=1
        while l2!=None:
            y=y+l2.val*temp
            temp*=10
            l2 = l2.next
        x+=y
        head = ListNode(int(x%10))
        x= int(x//10)
        firstNode = head
        while x!=0:
            dummyNode = ListNode(x%10)
            firstNode.next = dummyNode
            firstNode = dummyNode
            x=int(x//10)
        return head