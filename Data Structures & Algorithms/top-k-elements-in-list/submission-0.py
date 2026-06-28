class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lib = {}
        for number in nums:
            if number not in lib:
                lib[number] = 1
            else:
                lib[number] += 1
        result = sorted(lib.items(), key = lambda item: item[1], reverse=True)
        return [key for key, value in result][:k]