class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack=[]

        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top_t, top_i = stack.pop()
                res[top_i] = i-top_i
            stack.append([t,i])

        return res
        