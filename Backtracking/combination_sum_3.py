class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        def backtracking(combination, sum_nums, it):
            if len(combination) == k:
                if sum_nums == n:
                    res.append(combination[:])
                return

            for i in range(it, 10):
                combination.append(i)
                sum_nums += i
                backtracking(combination, sum_nums, i+1)
                sum_nums -= i 
                combination.pop()
        
        backtracking([], 0, 1)
        return res