class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]: #left side of array is sorted
                if nums[left] <= target < nums[mid]: #target belongs in between left and mid
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else: 
                    right = mid -1
        return -1
