class Solution(object):
    # DFS solution had cycle formation, did not work. This approach follows 2 time DP.
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        out = [[float('inf') for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    out[r][c] = 0
                else:
                    if r > 0:
                        out[r][c] = min(out[r][c], out[r-1][c] + 1)
                    if c > 0:
                        out[r][c] = min(out[r][c], out[r][c-1] + 1)
                        
        for r in range(len(mat)-1, -1, -1):
            for c in range(len(mat[0])-1, -1, -1):
                if mat[r][c] != 0:
                    if r + 1 < len(mat):
                        out[r][c] = min(out[r][c], out[r+1][c] + 1)
                    if c + 1 < len(mat[0]):
                        out[r][c] = min(out[r][c], out[r][c+1] + 1)
        return out