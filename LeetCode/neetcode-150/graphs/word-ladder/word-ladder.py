class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        n = len(wordList)

        def diff_one(w1, w2):
            n = len(w1)
            matches = 0
            for i in range(n):
                matches += w1[i] == w2[i]
            return matches == n - 1

        for i in range(n):
            for j in range(i + 1, n):
                if diff_one(wordList[i], wordList[j]):
                    edges[wordList[i]].append(wordList[j])
                    edges[wordList[j]].append(wordList[i])
            if diff_one(beginWord, wordList[i]):
                edges[beginWord].append(wordList[i])
                edges[wordList[i]].append(beginWord)      

        visit = set()
        def bfs():
            q = deque([[beginWord, ""]])
            level = 1
            while q:
                for i in range(len(q)):
                    word, prev = q.popleft()
                    if word == endWord:
                        return level
                    for close in edges[word]:
                        if close != prev and close not in visit:
                            visit.add(close)
                            q.append([close, word])
                level += 1
            return 0
        
        return bfs() 

