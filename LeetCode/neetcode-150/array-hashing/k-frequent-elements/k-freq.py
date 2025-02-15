class Solution(object):
    def topKFrequentB(self, nums, k):
        freq = {}

        buckets = []
        n = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            buckets.append([])
            n += 1

        for num, f in freq.items():
            buckets[f - 1].append(num)

        k_freq = []
        cnt = 0
        for i in range(n - 1, -1, -1):
            if buckets[i] == []:
                continue
            for num in buckets[i]:
                k_freq.append(num) 
                cnt += 1
                if cnt == k:
                    break
            if cnt == k:
                break

        return k_freq
                

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        k_freq = []
        heap_len = 0
        for item in freq.items():
            if heap_len < k:
                k_freq.append(item)
                heap_len += 1
                i = heap_len
                while i > 1:
                    u = i // 2
                    if u >= 1 and k_freq[u - 1][1] > item[1]:
                        k_freq[u - 1], k_freq[i - 1] = k_freq[i - 1], k_freq[u - 1]
                        i = u
                    else:
                        break
            else:
                if k_freq[0][1] > item[1]:
                    continue
                k_freq[0] = item
                i = 1
                while i < k:
                    j = i
                    l = i * 2
                    if l <= k and k_freq[l - 1][1] < k_freq[j - 1][1]:
                        j = l
                    r = i * 2 + 1
                    if r <= k and k_freq[r - 1][1] < k_freq[j - 1][1]:
                        j = r
                    if j == i:
                        break
                    k_freq[j - 1], k_freq[i - 1] = k_freq[i - 1], k_freq[j - 1]
                    i = j

        return [item[0] for item in k_freq]
        '''
        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        sorted_items = sorted_items[:k]
        return [item[0] for item in sorted_items]
        '''
