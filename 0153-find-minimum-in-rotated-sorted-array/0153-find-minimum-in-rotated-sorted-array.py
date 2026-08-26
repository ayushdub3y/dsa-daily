class Solution:
    def findMin(self, nums: List[int]) -> int:
        #basically the minimum element comes to the location of the k'th element of the array where k is the minimum number of times an array is rotated, classic binary search problem
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) //2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


