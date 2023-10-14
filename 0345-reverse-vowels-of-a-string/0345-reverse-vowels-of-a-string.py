class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list('aeiouAEIOU')
        left = len(s)-1
        right = 0
        s = list(s)
        while right < left:
            if s[right] not in vowels:
                right+=1
            elif s[left] not in vowels:
                left-=1
            else:
                s[left], s[right] = s[right] , s[left]
                left -= 1
                right +=1
        s = ''.join(s)
        return s