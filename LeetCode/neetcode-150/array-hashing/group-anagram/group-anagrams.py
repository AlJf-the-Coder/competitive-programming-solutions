class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n_strs = len(strs)
        anagram_groups = []
        hashes = [self.hash(string) for string in strs]
        classes = [-1 for _ in range(n_strs)]
        for i, (string, hash) in enumerate(zip(strs, hashes)):
            if classes[i] == -1:
                anagram_groups.append([string])
                for j in range(i + 1, n_strs):
                    j_string = strs[j]
                    j_hash = hashes[j]
                    if hash == j_hash:
                        classes[j] = i
                        anagram_groups[-1].append(j_string)

        return anagram_groups

    def hash(self, s):
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        return s_dict
