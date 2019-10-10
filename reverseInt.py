class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        initial = str(x)
        reverse = ""
        neg_limit = -0x80000000
        pos_limit = 0x7fffffff
        
        if initial[0] == "-":
            reverse += "-"
            initial = initial[1:]
        
        for i in reversed(range(len(initial))):
            reverse += initial[i]
        
        if len(reverse) > 1:
            if reverse[0] == "0":
                reverse = reverse[1:]
        
        if len(reverse) > 1:
            if reverse[0] == "-" and reverse[1] == "0":
                reverse = reverse[0] + reverse[2:]
            
        final = int(reverse)
        
        if final > pos_limit or final < neg_limit:
            return 0
        
        return final;
        