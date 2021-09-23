class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        
        dicts = {}
        for i in range(len(nums)):
            if ((target - nums[i]) in dicts) and i != dicts[target - nums[i]]:
                return [i, dicts[target - nums[i]]]
            dicts[nums[i]] = i