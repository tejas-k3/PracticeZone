"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Approach :-
Using two pointer approach
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slowPointer = head
        fastPointer = head
        val = 0
        while fastPointer!=None:
            if fastPointer.next == None:
                val+=1
                break
            fastPointer = fastPointer.next.next
            val+=2
        val-=n
        if val==0:
            slowPointer = slowPointer.next
            return slowPointer
        while val!=0:
            val-=1
            if val==0:
                slowPointer.next = slowPointer.next.next
            slowPointer = slowPointer.next
        return head