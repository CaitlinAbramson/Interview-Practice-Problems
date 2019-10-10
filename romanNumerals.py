class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0 
        
        for i in range(len(s)):
            if s[i] == "I":
                if i < len(s)-1:
                    if s[i+1] == "V":
                        num = num + 4
                    elif s[i+1] == "X":
                        num = num + 9
                    else: 
                        num = num + 1
                else:
                    num = num + 1
            elif s[i] == "V":
                if i > 0 and s[i-1] == "I":
                    num = num 
                else:
                    num = num + 5
            elif s[i] == "X": 
                if i > 0 and s[i-1] == "I":
                    num = num 
                else:
                    if i < len(s)-1:
                        if s[i+1] == "L":
                            num = num + 40
                        elif s[i+1] == "C":
                            num = num + 90
                        else:
                            num = num + 10
                    else:
                        num = num + 10
            elif s[i] == "L":
                if i > 0 and s[i-1] == "X":
                    num = num
                else:
                    num = num + 50
            elif s[i] == "C":
                if i > 0 and s[i-1] == "X":
                    num = num 
                else:
                    if i < len(s)-1:
                        if s[i+1] == "D":
                            num = num + 400
                        elif s[i+1] == "M":
                            num = num + 900
                        else:
                            num = num + 100
                    else:
                        num = num + 100
            elif s[i] == "D":
                if i > 0 and s[i-1] == "C":
                    num = num
                else:
                    num = num + 500   
            elif s[i] == "M":
                if i > 0 and s[i-1] == "C":
                    num = num
                else:
                    num = num + 1000
            else:
                raise Exception("not a valid Roman numeral")
        
        return num