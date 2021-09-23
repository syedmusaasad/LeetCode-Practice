class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        
        dicts = {}
        for i in range(len(nums)):
            dicts[nums[i]] = 0
        for i in range(len(nums)):
            if ((target - nums[i]) in dicts) and i != nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]