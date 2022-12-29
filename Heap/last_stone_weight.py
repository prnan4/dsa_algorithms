import heapq

# Tested in Tusimple coding assesment
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # Write your code here
        weights = stones
        weights.sort()
        while len(weights) > 1:
            w1 = weights[-1]
            w2 = weights[-2]
            diff = w1 - w2
            weights.pop()
            weights.pop()
            if diff > 0: 
                if not weights:
                    weights = [diff]
                elif diff >= weights[-1]:
                    weights.insert(len(weights), diff)
                else:
                    for i in range(len(weights)):
                        if diff < weights[i]:
                            weights.insert(i, diff)
                            break

        return weights[0] if len(weights) == 1 else 0

    # Using Heap
    # Pop operation in heap generally returns minimum element present
    def lastStoneWeight2(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(0, len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            w1 = - (heapq.heappop(stones))
            w2 = - (heapq.heappop(stones))
            diff = abs(w1 - w2)
            if diff > 0: 
                heapq.heappush(stones, - diff)
        return - stones[0] if len(stones) == 1 else 0