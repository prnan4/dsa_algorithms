class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs(r, c):
            if visited[r][c]:
                return
            visited[r][c] = True
            if grid[r][c] == "0":
                return
            
            if r > 0: dfs(r-1, c) # Go top
            if c + 1 < len(grid[0]): dfs(r, c+1) # Go right
            if r + 1 < len(grid): dfs(r+1, c) # Go bottom
            if c > 0: dfs(r, c-1) # Go left
                
        count_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not visited[r][c] and grid[r][c] == "1":
                    dfs(r, c)
                    count_islands += 1

        return count_islands