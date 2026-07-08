class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        column_size = len(matrix)
        row_size = len(matrix[0])

        low = 0
        high = row_size*column_size - 1

        while high >= low:
            mid = low + (high-low)//2

            r = mid // row_size
            c = mid % row_size
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return False