class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        components = [-1] * n
        def find(i):
            if components[i] < 0:
                return i
            components[i] = find(components[i])
            return components[i]
        def union(i, j):
            ri = find(i)
            rj = find(j)
            if ri == rj:
                return False
            if components[ri] < components[rj]:
                components[ri] += components[rj]
                components[rj] = ri
            else:
                components[rj] += components[ri]
                components[ri] = rj     
            return True 
                
        for a, b in edges:
            if not union(a, b):
                return False
        cnt = 0
        for c in components:
            if c < 0:
                cnt += 1
        return cnt == 1

class Solution1:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = [[] for i in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        marked = [False] * n
        def dfs(i, prev):
            if marked[i]:
                return False
            marked[i] = True
            for j in adjacency_list[i]:
                if j != prev and not dfs(j, i):
                    return False
            return True
        return dfs(0, -1) and all(marked)
            
