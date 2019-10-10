class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLen = float('inf')
        prefix = ""
        
        if not strs:
            return prefix
        
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        
        for i in range(0, minLen):
            val = strs[0][i]
            for s in strs:
                if s[i] != val:
                    return prefix
            prefix += val
        
        return prefix
                
            
                