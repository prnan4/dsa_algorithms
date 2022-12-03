class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        low = 0
        high = len(people) - 1
        while low <= high:
            if people[low] + people[high] <= limit:
                low += 1
                high -= 1
            else:
                high -= 1
            boats += 1
        return boats
            
        
        