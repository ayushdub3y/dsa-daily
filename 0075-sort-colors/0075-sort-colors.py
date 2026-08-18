class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hashmap = {0:0, 1:0, 2:0}

        for num in nums:
            hashmap[num] +=1
        
        nums.clear()

        for i in range(hashmap[0]):
            nums.append(0)
        for i in range(hashmap[1]):
            nums.append(1)
        for i in range(hashmap[2]):
            nums.append(2)