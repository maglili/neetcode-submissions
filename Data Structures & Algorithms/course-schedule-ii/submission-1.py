class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjcent tbl
        adj_tbl = defaultdict(list)
        for cour, preq in prerequisites:
            adj_tbl[cour].append(preq)

        res = []
        cycle = set()  # cur visit
        visit = set()
    
        def dfs(course) -> bool:
            if course in cycle:
                return False

            if course in visit:
                return True

            cycle.add(course)
            for preq in adj_tbl[course]:
                if not dfs(preq):
                    return False

            cycle.remove(course)
            visit.add(course)
            res.append(course)
            return True

        for cour in range(numCourses):
            if not dfs(cour):
                return []

        return res
