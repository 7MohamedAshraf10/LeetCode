class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        #iterate over the string of roman symbols
        for i in range(len(s)):
            #cheack wheather the current character's value is less than the value of the next character (if there is a next character).
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                # it means the current character represents a smaller value before a larger value
                #(e.g., 'IV' for 4 or 'IX' for 9 in Roman numerals).
                #In this case, the value of the current character is subtracted from the result 
                result -= m[s[i]]
            else:

                result += m[s[i]]
        return result