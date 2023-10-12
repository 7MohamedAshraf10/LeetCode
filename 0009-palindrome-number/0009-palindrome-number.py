class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        

        for i in range(len(digits)//2):
            if digits[i] != digits[len(digits)-i-1]:
                return False
        
        return True