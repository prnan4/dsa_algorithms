class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        truster = set()
        trustee = {}
        for i in range(1, n+1):
            truster.add(i)
            trustee[i] = 0
        print(trustee)
        for i in range(0, len(trust)):
            if trust[i][0] in truster:
                truster.remove(trust[i][0])
            trustee[trust[i][1]] += 1
        
        if len(truster) == 1 and trustee[list(truster)[0]] == n-1:
            return list(truster)[0]
        else:
            return -1