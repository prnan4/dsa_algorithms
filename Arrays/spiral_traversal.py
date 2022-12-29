class Solution(object):
    def go_right(self, matrix, spiral_traversal):
        spiral_traversal.extend(matrix.pop(0))
        return spiral_traversal
    
    def go_left(self, matrix, spiral_traversal):
        left_column = matrix.pop(-1)
        left_column.reverse()
        spiral_traversal.extend(left_column)
        return spiral_traversal
    
    def go_bottom(self, matrix, spiral_traversal):
        spiral_traversal.extend([r.pop(-1) for r in matrix])
        return spiral_traversal
    
    def go_top(self, matrix, spiral_traversal):
        top_row = [r.pop(0) for r in matrix]
        top_row.reverse()
        spiral_traversal.extend(top_row)
        return spiral_traversal
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_traversal = []
        num_elements = len(matrix[0]) * len(matrix)
        while num_elements != len(spiral_traversal):
            spiral_traversal = self.go_right(matrix, spiral_traversal)
            if num_elements != len(spiral_traversal): self.go_bottom(matrix, spiral_traversal)  
            if num_elements != len(spiral_traversal): self.go_left(matrix, spiral_traversal)  
            if num_elements != len(spiral_traversal): self.go_top(matrix, spiral_traversal)  

        return spiral_traversal

