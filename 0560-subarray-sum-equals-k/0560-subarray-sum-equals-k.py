class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_prefix = 0
        hash = {0:1} #for every array an empty subarray exists with sum = 0 before 1st element

        for i in range(len(nums)):
            current_prefix += nums[i]
            diff = current_prefix - k
            #calculate prefix sums for each element as we iterate i and check whether prefix sum is available if yes then increment its count value by 1, if no then append it to the hash. res will be equal to the count of 0 + count of diff in hash
            if diff in hash:
                res += hash[diff]
            hash[current_prefix] = hash.get(current_prefix, 0) + 1
        return res
            
        