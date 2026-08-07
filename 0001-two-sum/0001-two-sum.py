class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hash:
                return [i, hash[complement]]
            else:
                hash[nums[i]] = i 
        return []           