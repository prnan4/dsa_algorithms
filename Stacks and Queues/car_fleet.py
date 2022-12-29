class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x:x[0])
        
        fleets = []
        for pos, speed in sorted(pos_speed)[::-1]:
            time_taken = float(target-pos)/speed
            if (len(fleets) > 0) and time_taken <= fleets[-1]:
                continue
            fleets.append(time_taken)
        return(len(fleets))
        
            
        