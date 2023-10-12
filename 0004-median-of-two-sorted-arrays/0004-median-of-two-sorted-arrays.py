class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        newList = []
        i1 = i2 =0
        while i1 < m and i2 < n:
            if nums1[i1] < nums2[i2]:
                newList.append(nums1[i1])
                i1 += 1
            else:
                newList.append(nums2[i2])
                i2 += 1

        while i1 < len(nums1):
            newList.append(nums1[i1])
            i1 += 1
        

        while i2 < len(nums2):
            newList.append(nums2[i2])
            i2 += 1
           

        if len(newList) %2 ==0:
            index = len(newList) // 2
            median = (newList[index] + newList[index-1]) /2
        else: 
            median = float(newList[len(newList)//2])
        return median
