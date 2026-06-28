class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        right = n-1
        left = 0
        area = 0
        for i in range(n):
            new_area = min(heights[left],heights[right])*(right-left)
            if new_area > area:
                area = new_area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return area