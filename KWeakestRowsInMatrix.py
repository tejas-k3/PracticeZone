# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        stack = [] # no_of_soldiers, index
        index = 0
        for row in mat:
            no_of_soldiers = sum(1 for i in row if i == 1)
            val = (no_of_soldiers, index)
            if len(stack) == 0:
                stack.append(val)
            else:
                temp_stack = []
                while True:
                    last_element = stack.pop()
                    if ((last_element[0] > val[0]) or (last_element[0] == val[0] and last_element[1] > val[1])):
                        stack.append(last_element)
                        break
                    temp_stack.append(last_element)
                    if (len(stack) == 0):
                        break
                stack.append(val)
                while temp_stack:
                    stack.append(temp_stack.pop())
            index+=1
        ans = []
        while k:
            ans.append(stack.pop()[1])
            k-=1
        return ans