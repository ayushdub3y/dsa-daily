class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = []
        n = len(nums)
        answer = [-1] * n
        
        for i in range(n*2):
            index = i % n
            while stack and nums[index] > nums[stack[-1]]:
                waitingIndex = stack.pop()
                answer[waitingIndex] = nums[index]
        
            if i < n:
                stack.append(index)

        return answer








        