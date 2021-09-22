class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentMax = 0
        max = 0
        for element in nums:
            if element == 1:
                max += 1
            else:
                max = 0
            if max > currentMax:
                currentMax = max
        return currentMax