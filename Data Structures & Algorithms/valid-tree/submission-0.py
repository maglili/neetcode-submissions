class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # base case
        if n == 0:
            return True

        # build adjacent table
        adj = defaultdict(list)
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visit = set()

        def dfs(n, prev_n):
            if n in visit:
                return False

            visit.add(n)

            for nei in adj[n]:
                if nei == prev_n:
                    continue
                if not dfs(nei, n):
                    return False

            return True

        return dfs(0, None) and len(visit) == n
