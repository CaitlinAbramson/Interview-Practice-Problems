class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            val = target - nums[i]
            for j in range(0, len(nums)):
                if j != i:
                    if nums[j] == val:
                        return ([i, j])
        raise Exception("No solution")
                