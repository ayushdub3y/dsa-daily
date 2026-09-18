class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int: 
        #push element if stack is empty or the following element is greater than the top element
        #pop if next element's height is shorter than the top element until the height of element is greater than the top element or the array is empty
        #before popping, calculate area and best area for the elements from left to right
        #calculate height by current height and width by subtracting right minimmum element and left minimum element and subtract that by 1

        areaStack = []
        bestArea = 0
        heights.append(0) #sentinel element to calculate all amortizing areas
        n = len(heights)

        for i in range(n):
            start = i

            while areaStack and areaStack[-1][0] > heights[i]:
                height, oldStart = areaStack.pop()
                width = i - oldStart
                area = height * width
                bestArea = max(bestArea, area)

                start = oldStart
            areaStack.append([heights[i], start])
        return bestArea



        