class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lib = set()
        for element in nums:
            if element in lib:
                return True
            else:
                lib.add(element)
        return False