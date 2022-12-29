class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0])

        col_arr = [r[0] for r in matrix]

        # Binary search over first column 
        high = m -1
        low = 0

        while high >= low:
            mid = (high + low ) // 2
            if target == col_arr[mid]:
                return True
            elif target < col_arr[mid]:
                high = mid -1
            else:
                low = mid + 1
        
        row_arr = matrix[high]

        # Binary search over desired row
        high = n -1
        low = 0

        while high >= low:
            mid = (high + low ) // 2
            if target == row_arr[mid]:
                return True
            elif target < row_arr[mid]:
                high = mid -1
            else:
                low = mid + 1
        return False