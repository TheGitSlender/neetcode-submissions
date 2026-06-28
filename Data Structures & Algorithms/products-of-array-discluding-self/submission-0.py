class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        if 0 not in nums:
            product = 1
            for number in nums:
                product *= number
            for number in nums:
                result.append(product//number)
            return result
        else:
            index = nums.index(0)
            product = 1
            for i in range(len(nums)):
                if i == index:
                    continue
                product *= nums[i]
            for i in range(len(nums)):
                result.append(0) if i != index else result.append(product)
            return result
