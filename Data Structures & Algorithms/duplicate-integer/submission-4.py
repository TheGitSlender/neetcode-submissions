class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for element in nums:
            if element not in visited:
                visited.add(element)
            else:
                return True
        return False