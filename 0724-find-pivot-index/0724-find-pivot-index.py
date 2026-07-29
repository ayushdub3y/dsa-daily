class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  
        left_answer = 0
        total = sum(nums)
        for i in range(len(nums)):
            right_answer = total - nums[i] - left_answer
            if left_answer == right_answer:
                return i
            left_answer += nums[i]
        return -1
            


        