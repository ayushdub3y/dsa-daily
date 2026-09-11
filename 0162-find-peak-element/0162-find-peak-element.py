class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r= 0, len(nums) - 1
    #basically a simple check for a peak element is to check whether tthe element peak we are looking at is greater  than nums[peak-1] and nums[peak+1], but the real question is how do we find a peak element using binary search in an unsorted array?
    #genuinely speaking, it is kind of obvious that to solve this question, the element before the peak element and the peak element are bound to be sorted to form a peak element and the element after peak element is smaller than the peak element or maybe both depending upon the size.
    #question explicitly says that the element outside the array is strictly smaller than the first or last element of the array so we can use that for our reference
        while l<r:
            mid = (l+r) // 2
            #chatgpt helped me by giving me this hint that boosted my intuition, using slope to move our binary search where we move according to mid+1 element's direction.
            if nums[mid+1] < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l

            
      # if the peak found to be right, for example if nums[mid] < nums[mid + 1] then we move left pointer at mid or mid - 1 to find peak
      #if the peak is found to be left that means if nums[mid+1] < nums[mid] then we move right pointer at mid -1  