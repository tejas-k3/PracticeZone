"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Approach -
Iterate through the list with a pointer and keep a pointer on head
if duplication is found, remove that pointer from the list by changing
the reference from duplicated node to the node next to it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return  head
        tempNode = head
        nNode = head.next
        while nNode!=None:
            if nNode.val == tempNode.val:
                tempNode.next=nNode.next
            else:
                tempNode=nNode
            nNode=nNode.next
        return head
