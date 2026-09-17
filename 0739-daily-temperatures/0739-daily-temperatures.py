class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #implement a stack to show the forecast of the upcoming weather like basically finding at what distance is the greater element of temperatures exists, as j - i
        i = 0
        helperStack, answer = [], [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            #if stack is empty append that element
            while helperStack and temperatures[i] >= temperatures[helperStack[-1]]:
                helperStack.pop()
            if helperStack:
                answer[i] = helperStack[-1] - i
            helperStack.append(i)
        return answer
                


        