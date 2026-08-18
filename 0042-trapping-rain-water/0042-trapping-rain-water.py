class Solution:
    def trap(self, height: List[int]) -> int:
        #the two pointer apporach describes maintaining two pointers from left to right where the local maximum or current maximum on both sides will allow us to help us calculate the amount of water
        #we will increment the left pointer if height at left is smaller than right and vice versa.
        n = len(height)
        left, right = 0, n-1
        left_max, right_max = height[0], height[n-1]
        res= 0

        while left < right:
            if left_max < right_max:
                left+=1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -=1
                right_max = max(right_max, height[right])
                res += right_max - height[right]
        return res
