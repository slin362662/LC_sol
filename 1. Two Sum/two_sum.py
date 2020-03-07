class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        num_index = {}
        for i in range(len(nums)):
            if (target - nums[i]) in num_index:
                return [i, num_index[target-nums[i]]]
            else:
                num_index[nums[i]] = i
        return []