class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        nextGreater = {}

        # Build next-greater relationships using nums2
        for num in nums2:

            # Current number is greater than the book on top
            while stack and num > stack[-1]:
                smaller = stack.pop()
                nextGreater[smaller] = num

            stack.append(num)

        # Anything still in the stack has no next greater element
        while stack:
            num = stack.pop()
            nextGreater[num] = -1

        # nums1 simply asks for its answers
        answer = []

        for num in nums1:
            answer.append(nextGreater[num])

        return answer