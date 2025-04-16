class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(edge) for edge in edges)
        components = [-1] * (n + 1)
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
                
        for edge in edges:
            if not union(*edge):
                return edge
        return []

class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = max(max(edge) for edge in edges)
        for i in range(len(edges) - 1, - 1, -1):
            if self.validTree(n + 1, edges, i):
                return edges[i]
        return []

    def validTree(self, n: int, edges: List[List[int]], skip: int) -> bool:
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
                
        for i, (a, b) in enumerate(edges):
            if i == skip:
                continue
            if not union(a, b):
                return False
        cnt = 0
        for c in components:
            if c < 0:
                cnt += 1
        return cnt - 1 == 1
