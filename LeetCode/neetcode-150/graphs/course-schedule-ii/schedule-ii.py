class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = defaultdict(list)
        indegrees = [0] * n
        for a, b in prerequisites:
            dependencies[b].append(a)
            indegrees[a] += 1

        def bfs(q):
            res = []
            while q:
                for i in range(len(q)):
                    s = q.popleft()
                    if seen[s]:
                        return False
                    if marked[s]:
                        return True
                    seen[s] = True
                    for d in dependencies[s]:
                        indegrees[d] -= 1
                        if not indegrees[d]:
                            q.append(d)
                    res.append(s)
                    marked[s] = True
                    seen[s] = False
            return res if len(res) == n else []

        seen = [False] * numCourses
        marked = [False] * numCourses
        q = []
        for c in range(numCourses):
            if not indegrees[c]:
                q.append(c)
        return bfs(q)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependencies = defaultdict(list)
        for a, b in prerequisites:
            dependencies[a].append(b)
        res = []
        def dfs(s):
            if seen[s]:
                return False
            if marked[s]:
                return True
            seen[s] = True
            for d in dependencies[s]:
                if not dfs(d):
                    return False
            res.append(s)
            marked[s] = True
            seen[s] = False
            return True

        seen = [False] * numCourses
        marked = [False] * numCourses
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
