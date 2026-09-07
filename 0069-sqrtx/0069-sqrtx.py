class Solution:
    def mySqrt(self, x: int) -> int:
        #we can check for an integer called target, if target*target[i] is less than x and target*target[i+1] is greater than or equal to x then we can just apply simple binary search approach to solve it
        l, r = 0, x

        while l<=r:

            mid = (l+r)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return mid-1 if mid*mid > x else mid
                
        