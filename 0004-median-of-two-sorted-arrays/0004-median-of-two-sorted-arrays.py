class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsx = nums1 + nums2
        numsx = sorted(numsx)
        l, r = 0, len(numsx)
        mid = (l+r) // 2
        if len(numsx) % 2 == 0:
            med = (numsx[mid-1] + numsx[mid]) / 2
        else:
            med = numsx[mid]
        return med
#brute
        