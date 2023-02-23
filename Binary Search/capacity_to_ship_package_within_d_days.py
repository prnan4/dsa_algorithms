class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        l = max(weights)
        r = sum(weights)

        while l <= r:
            if l == r:
                return l
            mid = (l+r) / 2
            subsum = 0
            trial_days = 1
            for w in weights:
                if subsum + w <= mid:
                    subsum += w
                else:
                    trial_days += 1
                    subsum = w
            if trial_days <= days:
                r = mid
            else:
                l = mid + 1
            
     
        

