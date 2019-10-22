class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        # Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        
        if not nums:
            return len(nums)
        
        unique_count = 1
        
        for i in range(len(nums)-1):
            num1 = nums[i]
            num2 = nums[i+1]
            if num1 < num2:
                nums[unique_count] = num2
                unique_count += 1
        
        nums = nums[0:unique_count]
        return len(nums)
        
        
          

        