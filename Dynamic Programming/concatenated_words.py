class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        def wordBreak(word, preWords):
            dp = [False for _ in range(len(word) + 1)]
            dp[0] = True
            for i in range(1, len(word)+1):
                for j in range(0, i):
                    if dp[j] and word[j:i] in preWords:
                        dp[i] = True
                        break
            return dp[len(word)]

        words = sorted(words, key=len)
        res = []
        preWords = set()
        
        for w in words:
            if wordBreak(w, preWords):
                res.append(w)
            preWords.add(w)
        return res
