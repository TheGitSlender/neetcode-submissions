class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix_max = [0] * n
        suffix_max = [0] * n

        temp_max = 0
        for i in range(n):
            if height[i] > temp_max:
                temp_max = height[i]
            prefix_max[i] = temp_max
        temp_max = 0
        for i in range(n-1,-1,-1):
            if height[i] > temp_max:
                temp_max = height[i]
            suffix_max[i] = temp_max

        result = 0
        for i in range(n):
            result += min(prefix_max[i], suffix_max[i]) - height[i]

        return result