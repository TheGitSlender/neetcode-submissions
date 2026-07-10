class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        high = rows*columns - 1
        low = 0

        while high >= low:
            mid = (high + low)//2
            r = mid//columns
            c = mid%columns
            if target == matrix[r][c]:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False