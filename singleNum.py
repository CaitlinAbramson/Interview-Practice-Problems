class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        for i in nums:
            key = i
            if key in hashMap:
                hashMap.pop(key)
            else:
                hashMap.update({key : i})
        
        return hashMap.values()[0]
        
            