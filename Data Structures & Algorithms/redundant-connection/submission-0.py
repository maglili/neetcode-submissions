class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]  # 預設自己是自己的 parent
        rank = [1 for i in range(N + 1)]

        def find(node) -> int:
            if par[node] != node:
                par[node] = find(par[node])  # path compression: 把 parent 都改成最上面那個
            return par[node]

        def union(n1, n2) -> bool:
            root1, root2 = find(n1), find(n2)

            if root1 == root2:  # 早已連在一起
                return False

            if rank[root1] < rank[root2]:
                root1, root2 = root2, root1

            rank[root1] += rank[root2]
            par[root2] = root1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        return []
