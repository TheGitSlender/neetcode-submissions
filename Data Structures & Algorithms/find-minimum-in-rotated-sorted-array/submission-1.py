class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0
        while high >= low:
            mid = (high+low)//2
            if mid != 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] > nums[low]:
                low = mid +1
            else:
                high = mid - 1
        return nums[0]
            