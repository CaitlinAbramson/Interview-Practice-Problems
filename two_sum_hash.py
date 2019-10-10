class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(0, len(nums)):
            val = target - nums[i]
            print(val)
            if val in d:
                return [d[val], i]
            else:
                d.update({nums[i] : i})
              