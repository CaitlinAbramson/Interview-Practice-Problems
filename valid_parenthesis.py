class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        count = 0
        balanced = False
        
        if s == "":
            return True
        
        for bracket in s:   
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)
                count += 1
            else:
                if not stack:
                    return False
                else:
                    match = stack.pop()
                    count += 1
                    if match == "(" and bracket == ")":
                        balanced = True
                    elif match == "{" and bracket == "}":
                        balanced =  True
                    elif match == "[" and bracket == "]":
                        balanced = True
                    else:
                        return False
        
        if stack or count < len(s):
            return False
        
        return balanced
        