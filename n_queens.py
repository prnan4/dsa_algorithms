class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        columns = set()
        pos_diagonal = set()
        neg_diagonal = set()
        result = []
        board = [['.'] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
            for c in range(n):
                if c in columns or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
                    continue
                
                columns.add(c)
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                columns.remove(c)
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                board[r][c] = "."
                
        backtrack(0)
        return result
                
                
                
            
        