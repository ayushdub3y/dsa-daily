class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        freqMap = {}
        maxFreq = 0
        n = len(fruits)
        for j in range(n):
            freqMap[fruits[j]] = freqMap.get(fruits[j], 0) + 1
            #if hashmap stores more keys than 2, then we shrink the windoe by moving i and we keep reducing count until there are only two keys present in the hashmap
            while len(freqMap) > 2:
                freqMap[fruits[i]] -= 1
                if freqMap[fruits[i]] == 0:
                    del freqMap[fruits[i]]
                i+=1
            current_len = j - i + 1
            maxFreq = max(maxFreq, current_len)

        return maxFreq
