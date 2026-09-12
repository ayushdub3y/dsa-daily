class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l<r:
            added = numbers[l] + numbers[r]

            if target == added:
                return [l+1,r+1]
            elif target > added:
                l+=1
            else:
                r-=1
        return -1
#two pointer approach