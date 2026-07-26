class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjcent tbl
        adj_tbl = defaultdict(list)
        for cour, preq in prerequisites:
            adj_tbl[cour].append(preq)

        res = []
        visit = set()  # cur visit

        def dfs(course) -> bool:
            if course in visit:
                return False
            if adj_tbl[course] == []:
                return True

            visit.add(course)
            for preq in adj_tbl[cour]:
                if not dfs(preq):
                    return False

            adj_tbl[course] = []
            visit.remove(course)
            return True

        for cour in range(numCourses):
            res.append(cour)
            if not dfs(cour):
                return []

        return res
