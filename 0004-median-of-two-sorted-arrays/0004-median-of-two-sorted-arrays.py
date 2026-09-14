class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #there are some steps which seem complicated to solve this problem but once you get it, its basically muscle memory.
        #the goal is two divide the two given arrays into 2 parts each, 4 parts in total. by following the rule:
        #left1<=right2
        #left2<=right1
        #only then we can deal with the median and its quite simple actually
        #always search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = (len(nums1) + len(nums2))
        half = (total+1) //2

        l, r = 0, len(nums1)

        #now we use binary search
        while l<=r:
            partition1 = (l+r) // 2
            partition2 = half - partition1

            left1 = float("-inf") if partition1 == 0 else nums1[partition1-1]
            right1 = float("inf") if partition1 == len(nums1) else nums1[partition1]
            left2 = float("-inf") if partition2 == 0 else nums2[partition2-1]
            right2 = float("inf") if partition2 == len(nums2) else nums2[partition2]

            if left1<=right2 and left2<=right1:
                if total%2 == 1:
                    return max(left1, left2)
                return ((max(left1,left2) + min(right1,right2))/2)
            elif left1>right2:
                r = partition1 - 1
            else:
                l = partition1 + 1
