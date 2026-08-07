class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]] = i
        return False