class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. build adj tbl
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        res = 0

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

        for n in range(n):
            if n not in visit:
                dfs(n)
                res += 1

        return res