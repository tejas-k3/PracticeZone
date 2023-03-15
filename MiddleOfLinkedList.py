"""https://leetcode.com/problems/middle-of-the-linked-list/
Approach: Have two pointers, one fast runner one slow runner.
fast goes 2 steps slow goes 1 step.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = head
        while head.next is not None:
            mid = mid.next
            if head.next.next is None:
                return mid
            head = head.next.next
        return mid