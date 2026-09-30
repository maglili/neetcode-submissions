class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 1. Build adj list
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                des = abs(xi - xj) + abs(yi - yj)
                adj[i].append((des, j))
                adj[j].append((des, i))

        # prims algo
        minheap = [(0, 0)]
        seen = set()
        res = 0

        while len(seen) < len(points):
            cost, node = heapq.heappop(minheap)
            if node in seen:
                continue
            seen.add(node)
            res += cost

            for cost_nei, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(minheap, (cost_nei, nei))
        return res
