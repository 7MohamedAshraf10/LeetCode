class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # length of the list 
        n = len(gain)
        # list to get the altidute, and it's length = length of the gain + 1
        ans = [0]*(n+1)

        # iterate through each variable in gain list
        for i in range(n):
            # iterate through each value before the current value and sum them, and store them in the ans list
            for x in range(0 , i+1):
                ans[i] += gain[x]
        # return the max number in ans, which is the highest alitude
        return max(ans)