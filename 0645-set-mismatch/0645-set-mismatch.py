class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # the expected SUM Should ne 1+2+3+..+n can be caculated thru n(n+1)//2
        # The missing number will be = expected sum - actuall sum
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        num_set = set()
        duplicate = -1

        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)

        missing = expected_sum - (actual_sum - duplicate)
        return [duplicate, missing]