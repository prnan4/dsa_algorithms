class Solution(object):

    # DFS: Time limit exceeded
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        grid = [[ None for _ in range(n)] for _ in range(n)]
        for flight in flights:
            s, d, a = flight
            grid[s][d] = a
        min_amt = float('inf')
        
        min_a = []
        def rec(amt, stops, strt):
            if stops > k:
                return

            for i in range(0, n):
                if i != strt:  
                    print(strt, i, stops)             
                    if i == dst and grid[strt][dst] is not None:
                        min_a.append(amt + grid[strt][dst])
                    elif grid[strt][i] is not None:
                        rec(amt + grid[strt][i], stops + 1, i)
        rec(0, 0, src)
        if len(min_a) == 0:
            return -1
        else:
            return min(min_a)


    # BFS
    from collections import deque
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adj = [[] for _ in range(n)]
        
        for flight in flights:
            s, d, a = flight
            adj[s].append([d, a])

        dist = [float('inf') for i in range(n)]
        q = deque([[src, 0]])
        stops = 0
        while(q and stops <= k ):
            n = len(q)
            while(n):
                s, price = q.popleft()
                for i in range(len(adj[s])):
                    d, distance = adj[s][i]
                    if price + distance < dist[d]:
                        dist[d] = price + distance
                        q.append([d, dist[d]])
                n -= 1
            stops += 1
        
        return -1 if dist[dst] == float('inf') else dist[dst]
    
    # Dijkstra's 
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adj = [[] for _ in range(n)]
        
        for flight in flights:
            s, d, a = flight
            adj[s].append([d, a])

        dist = [float('inf') for i in range(n)]
        q = deque([[0, src, 0]])
        while(q):
            stops, s, price = q.popleft()
            if stops <= k:
                for i in range(len(adj[s])):
                    d, distance = adj[s][i]
                    if price + distance < dist[d]:
                        dist[d] = price + distance
                        q.append([stops + 1, d, dist[d]])
                
        print(dist)
        return -1 if dist[dst] == float('inf') else dist[dst]
    




        

        