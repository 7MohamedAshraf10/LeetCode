class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        n = len(gain)
        ans = [0]*(n+1)
        for i in range(n):
            for x in range(0 , i+1):
                ans[i] += gain[x]
        return max(ans)