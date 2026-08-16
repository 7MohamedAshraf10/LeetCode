class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if found zero save the old  max in variable, and ask if it's higher that the old one or not

        max = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
                if count > max:
                    max = count
            else:
                if max < count:
                    max = count
                count = 0
        return max