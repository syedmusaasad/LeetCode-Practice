class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prev, current = None, None
        i = 0
        while i < len(nums):
            current = nums[i]
            if current == prev:
                i -= 1
                nums.remove(nums[i])
            prev = current
            i += 1