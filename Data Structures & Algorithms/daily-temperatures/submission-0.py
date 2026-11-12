class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for l in range(n):
            # Check if current day is warmer than previous days
            while stack and temperatures[l] > temperatures[stack[-1]]:
                p = stack.pop()
                output[p] = l - p

            # Store current day's index
            stack.append(l)

        return output