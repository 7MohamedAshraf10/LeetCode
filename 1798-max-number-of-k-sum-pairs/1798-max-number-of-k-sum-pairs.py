class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_op = 0
        cur = 0
        last = len(nums) -1
        nums.sort()
        while cur < last:
            if (nums[cur] + nums[last]) == k and last > cur:
                max_op +=1
                last -=1
                cur +=1
            elif nums[cur] + nums[last] > k:
                last -=1
            else:
                cur +=1
        return max_op
