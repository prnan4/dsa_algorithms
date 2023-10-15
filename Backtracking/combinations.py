# October 15 2023
def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


        result = []

        def backtrack(combination, it):
            if len(combination) == k:
                result.append(combination[:])
                return 
            for i in range(it, n):
                num = i + 1
                combination.append(num)
                backtrack(combination, i +1)
                combination.pop()

        backtrack([], 0)
        return result
        