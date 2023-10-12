class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        # Check fo the int sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse Integer
        while x!=0:
            # get the last digit
            digit = x % 10
            # remove the last digit form the number
            x = x // 10
            # check overflow or underflow 32-bit
            if reverse > 2**31//10 or (reverse == 2**31//10 and digit > 7) or reverse < -2**31//10 or (reverse == -2**31//10 and digit < -8):
                return 0

            # update reversed int
            reverse = reverse*10 + digit
        # return reversed * sign
        return sign * reverse
        
        
        
        
       