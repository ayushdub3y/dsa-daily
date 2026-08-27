class Solution:

    #firstly we write a simple to decide whether in the current speed, can all the bananas be finished
    def canBeEaten(self, mid, h, piles) -> bool:
        hoursTaken = 0

        for i in range(len(piles)):
            hoursTaken += piles[i] // mid
            if(piles[i]%mid != 0):
                hoursTaken +=1
        return hoursTaken <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r)//2

            if self.canBeEaten(mid, h, piles):
                r = mid
            else:
                l = mid+1
        return l
        