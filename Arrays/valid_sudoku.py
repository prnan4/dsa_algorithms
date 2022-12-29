class Solution(object):

    # Approach 1
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for r in range(len(board)):
            row = set()
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
        
        
        for c in range(len(board[0])):
            col = set()
            for r in range(len(board)):
                if board[r][c] != ".":
                    if board[r][c] in col:
                        return False
                    else:
                        col.add(board[r][c])
        
        for i in range(3):
            r_index = ((i + 1) * 3) 
            for j in range(3):
                c_index = ((j + 1) * 3) 
                mat = [ board[k][c_index - 3: c_index] for k in range(r_index -3, r_index)]
                val = set()
                for m in range(len(mat)):
                    for n in range(len(mat[0])):
                        if mat[m][n] != ".":
                            if mat[m][n] in val:
                                return False
                            else:
                                val.add(mat[m][n])
                                
        return True

    # Approach 2   
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for r in range(len(board)):
            row = set()
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in row:
                        return False
                    else:
                        row.add(board[r][c])
        
        
        for c in range(len(board[0])):
            col = set()
            for r in range(len(board)):
                if board[r][c] != ".":
                    if board[r][c] in col:
                        return False
                    else:
                        col.add(board[r][c])
        
        for i in [3, 6, 9]:
            for j in [3, 6, 9]:
                print(i, j)
                mat = [ board[m][n] for m in range(i-3, i) for n in range(j-3, j)]
                sqr = set()
                for val in mat:
                    if val != ".":
                        if val in sqr:
                            return False
                        else:
                            sqr.add(val)
                        
                    
                                
        return True
        
        

                
                
        
        
        

                
                
        