# https://leetcode.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head, k):
        llLen = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            llLen += 1
        q, r = divmod(llLen, k)
        ans = []
        for i in range(k):
            size = q + 1 if (r := r - 1) >= 0 else q
            ans.append(head)
            last = None
            while size > 0:
                last = head
                head = head.next
                size -= 1
            if last: last.next = None
                
        return ans