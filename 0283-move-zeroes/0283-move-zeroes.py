class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i, j= 0, 0

        for j in range(len(nums)):
            # if i = 0 and j = 0 move both,
            #if i = 0, j != 0 swap.
            #if i != 0 and j != 0 move both
            #if i != 0 and j = 0, move j
            if nums[i] == 0 and nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i+=1
            elif nums[i] != 0 and nums[j] != 0:
                i+=1
            else:
                continue

        