def insert_heap(freq, k = 3):
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
                    j = -1
                    l = i * 2
                    if l <= k and k_freq[l - 1][1] < item[1]:
                        j = l
                    r = i * 2 + 1
                    if r <= k and k_freq[r - 1][1] < item[1]:
                        j = r
                    if j == -1:
                        break
                    k_freq[j - 1], k_freq[i - 1] = k_freq[i - 1], k_freq[j - 1]
                    i = j
        return [item[0] for item in k_freq]
