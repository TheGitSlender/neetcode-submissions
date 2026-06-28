class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for x in range(n):
            target = -nums[x]
            left = x+1
            right = n-1
            while left < right:
                temp = nums[right] + nums[left]
                if temp == target:
                    if [nums[x],nums[left],nums[right]] not in result:
                        result.append([nums[x],nums[left],nums[right]])
                    left += 1
                elif temp > target:
                    right -= 1
                else:
                    left += 1
        return result
            

