class Solution:
    def maxArea(self, height: List[int]) -> int:

        area = 0
        n = len(height)
        l, r = 0, n-1
        
        while l < r:

            length =  r - l
            breadth =  min(height[l], height[r])
            curr_area = length * breadth
            
            if height[l] < height[r]:
                l+=1
            
            elif height[r] <= height[l]:
                r-=1

            area = max(area, curr_area)

        return area
             

        