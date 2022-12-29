class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)
        cols = len(grid[0])
        rotten_q = []
        fresh = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        
        while rotten_q and fresh > 0:
            
            time += 1
            for _ in range(len(rotten_q)):  
                r, c = rotten_q.pop(0)
                
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    fresh -= 1
                    rotten_q.append((r-1, c))
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    fresh -= 1
                    rotten_q.append((r, c-1))
                if r < rows - 1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    fresh -= 1
                    rotten_q.append((r+1, c))
                if c < cols -1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    fresh -= 1
                    rotten_q.append((r, c+1))

        if fresh == 0:
            return time
        else:
            return -1