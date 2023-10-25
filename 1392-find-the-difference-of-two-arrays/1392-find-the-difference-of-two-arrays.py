class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        ans = []
        n1 = []
        n2 = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        for i in nums1:
            if i not in nums2:
                n1.append(i)
        for x in nums2:
            if x not in nums1:
                n2.append(x)
        ans.append(n1)
        ans.append(n2)
        return ans