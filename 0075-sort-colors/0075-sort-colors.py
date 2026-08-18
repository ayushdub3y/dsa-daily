class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid = 0,0
        n = len(nums) - 1
        high = n

        while mid <= high:
            if nums[mid] < 1:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else: #nums mid == 2
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1