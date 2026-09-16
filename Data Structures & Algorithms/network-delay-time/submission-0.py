class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adj list
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))

        seen = set()
        minheap = [(0, k)]
        res = 0

        while minheap:
            t, node = heapq.heappop(minheap)
            if node in seen:
                continue

            seen.add(node)
            res = max(t, res)

            for t_nei, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(minheap, (t_nei + t, nei))

        return res if len(seen) == n else -1
