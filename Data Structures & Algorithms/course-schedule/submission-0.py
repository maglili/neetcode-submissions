class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacent tbl
        adj_tbl = defaultdict(list)
        for cour, pre in prerequisites:
            adj_tbl[cour].append(pre)

        seen = set()
        def dfs(course):
            if course in seen:
                return False

            seen.add(course)
            for cour in adj_tbl[course]:
                if not dfs(cour):
                    return False
            return True
            
        # dfs on each class
        for cour, _ in prerequisites:
            if not dfs(cour):
                return False
        return True