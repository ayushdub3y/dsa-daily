class Solution:
    def trap(self, height: List[int]) -> int:
        #the first part is to write two helper functions to get ourselves the left max and right max for each index.
        #the second part is to find us for every ith index the height = min(lm[i], rm[i]) - h[i]and keep adding it to the  res

        res = 0
        n = len(height)

        def leftMax(height):
            maximum = [0] * len(height)
            running_max = height[0]
            maximum[0] = running_max
            for i in range(1, len(height)):
                running_max = max(running_max, height[i])
                maximum[i] = running_max
            return maximum
        
        def rightMax(height):
            maximum = [0] * len(height)
            running_max = height[n-1]
            maximum[n-1] = running_max

            for i in range(len(height)-2, -1, -1):
                running_max = max(running_max, height[i])
                maximum[i] = running_max
            return maximum
        left_max= leftMax(height)
        right_max =rightMax(height)

        for i in range(len(height)-1):
            heights = min(left_max[i], right_max[i]) - height[i]
            res+=heights
        return res   