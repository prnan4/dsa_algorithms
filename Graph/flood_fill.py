class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        no_rows = len(image)
        no_cols = len(image[0])
        
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        def dfs(r, c):
            if image[r][c] == originalColor:
                image[r][c] = color
                # Move top
                if r > 0: dfs(r-1, c)
                # Move left
                if c+1 < no_cols: dfs(r, c+1)
                # Move bottom
                if r+1 < no_rows: dfs(r+1, c)
                # Move right
                if c > 0: dfs(r, c-1)
                

                
        dfs(sr, sc)
        return image