class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        visited = [False] * (len(tickets))
        itinerary = []
        for i, (fro, to) in enumerate(tickets):
            adj_list[fro].append((to, i))
        for adjs in adj_list.values():
            adjs.sort()
        itinerary = []

        def backtrack(fro, count):
            itinerary.append(fro)
            if count == len(tickets):
                return True
            prev = None
            for to, i in adj_list[fro]:
                if visited[i] or to == prev:
                    continue
                visited[i] = True
                if backtrack(to, count + 1):
                    return True
                visited[i] = False
                prev = to
            return False

        backtrack("JFK", 0)
        return itinerary
