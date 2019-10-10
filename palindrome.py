class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
Brute Force: if negative number, return 0. if positive number, convert to string, iterate through from end. Compare each value to an iteration from the start. If not equal, return false. If all are equal, return true.
Run-time: O(n^2)

Challenge: do not turn it into string - compare half of the first int to its reversed second half
        How do it without using a string?
        Mod 10 will get the last digit
        Divide by 10 to move to next digit
        If odd number of digits, divide length in half and add 1
        If even number of digits, divide length in half
Run-time: O(logn) where n is the int
        """
        
        if x < 0:
            return False 
        if x >= 0 and x < 10:
            return True
        
        rev = 0
        original = x
        
        while x != 0:
            rev = (rev * 10) + (x % 10)
            x /= 10
        
        return rev == original
        
