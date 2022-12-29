class Solution(object):

    #========================== APPROACH 1 ==========================
    # DFS - Time Limit exceeded

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        p_map = {i:[] for i in range(numCourses)}
        for prereq in prerequisites:
            c, p = prereq
            p_map[c].append(p)
            
        visited = set()
        
        def dfs(c):
            if c in visited:
                return False
            if not p_map[c]:
                return True
            visited.add(c)
            for p in p_map[c]:
                if not dfs(p): 
                    return False
            visited.remove(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True