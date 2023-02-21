class Solution(object):
    # TLE
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        list_zip = zip(ages, scores)
        res = sorted(list_zip, key = lambda x: (x[0], x[1]))
        def recursive(player_ages, score, rem_ages):
            print(score, player_ages, rem_ages)
            if len(player_ages) > 1 and player_ages[-1][1] < player_ages[-2][1]:
                return 0
            if len(rem_ages) == 0:
                return score
            player_ages.append(rem_ages[0])
            include = recursive(player_ages, score + player_ages[-1][1], rem_ages[1:])
            player_ages.pop()
            dont_include = recursive(player_ages, score, rem_ages[1:])

            return max(include, dont_include)

        return recursive([], 0, res)