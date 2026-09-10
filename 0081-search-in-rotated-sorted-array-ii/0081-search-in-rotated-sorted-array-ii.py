class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #addition of duplicates may seem that the problem is getting easier but it actually makes it tougher. lets say we have an array nums  = {7, 9 ,11, 1, 3, 7} target = 3, if the elements at left, right, mid pointer are same, the binary condition just breaks and thats not good so we will have to manually move pointers by 1 at that case if they are not equal to target
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left] == nums[right]:
                left+=1
                right-=1
            elif nums[mid] >= nums[left]: #left side is sorted
                if nums[left] <= target <= nums[mid]: #check if in left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

            