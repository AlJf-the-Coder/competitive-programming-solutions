class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencies = defaultdict(list)
        for a, b in prerequisites:
            dependencies[a].append(b)

        def dfs(s):
            if seen[s]:
                return False
            if dependencies[s] == []:
                return True
            seen[s] = True
            for d in dependencies[s]:
                if not dfs(d):
                    return False
            dependencies[s] = []
            seen[s] = False
            return True

        seen = [False] * numCourses
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

