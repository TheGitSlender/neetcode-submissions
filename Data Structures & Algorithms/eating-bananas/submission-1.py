from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        high = max(piles)
        low = 1

        while high >= low:
            mid = (high+low)//2
            total_hours = sum([ceil(p/mid) for p in piles])
            if total_hours > h:
                low = mid + 1
            else:
                high = mid - 1
        return low
        