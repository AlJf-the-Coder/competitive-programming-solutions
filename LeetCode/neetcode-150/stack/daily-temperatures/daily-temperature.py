class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]
        stack = [(0, temperatures[0])]
        for i, temperature in enumerate(temperatures):
            if i == 0: continue
            answer.append(0)
            while stack and stack[-1][1] < temperature:
                j, _ = stack.pop()
                answer[j] = i - j
            stack.append((i, temperature))
        return answer
