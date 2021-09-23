class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        
        for i in range(len(nums)):
            try:
                potential = nums.index(target - nums[i])
                if (isinstance(nums[potential], int) and i != nums.index(target - nums[i])):
                    return [i, nums.index(target - nums[i])]
            except ValueError:
                continue