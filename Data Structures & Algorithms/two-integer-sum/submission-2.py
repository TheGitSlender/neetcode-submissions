class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        library = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in library:
                return [library[difference], i]
            else:
                library[n] = i
            