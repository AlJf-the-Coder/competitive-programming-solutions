class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                return
            if components[ri] < components[rj]:
                components[ri] += components[rj]
                components[rj] = ri
            else:
                components[rj] += components[ri]
                components[ri] = rj      
                
        for a, b in edges:
            union(a, b) 
        cnt = 0
        for c in components:
            if c < 0:
                cnt += 1
        return cnt
