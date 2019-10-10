class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 2*sum(set(nums))
        for i in nums:
            total -= i
        
        return total
        
            