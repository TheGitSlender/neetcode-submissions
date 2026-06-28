class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        new_nums = sorted(set(nums))
        left = 0
        right = 0
        length = 1
        for i in range(1,len(new_nums)):
            if new_nums[i] == new_nums[i-1] + 1:
                right += 1
            else:
                left, right = i, i
            if right - left + 1 > length:
                length = right - left + 1 
        return length
            