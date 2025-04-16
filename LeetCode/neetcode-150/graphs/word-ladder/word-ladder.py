from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        inters = defaultdict(list)

        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            list_word = list(word)
            for i in range(len(list_word)):
                tmp = list_word[i]
                list_word[i] = '*'
                joined = ''.join(list_word)
                inters[joined].append(word)
                edges[word].append(joined)
                list_word[i] = tmp

        def bfs():
            visit = set()
            q = deque([beginWord])
            visit.add(beginWord)
            level = 1
            while q:
                for i in range(len(q)):
                    word = q.popleft()
                    if word == endWord:
                        return level
                    for inter in edges[word]:
                        for close in inters[inter]:
                            if close not in visit:
                                visit.add(close)
                                q.append(close)
                level += 1
            return 0
        
        return bfs() 

class Solution1:
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

