class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freqs = Counter(hand)

        for num in hand:
            start = num
            while freqs[start - 1]:
                start -= 1
            while start <= num:
                while freqs[start]:
                    for i in range(groupSize):
                        if freqs[start + i] > 0:
                            freqs[start + i] -= 1
                        else:
                            return False
                start += 1
        return True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter()
        """
        freqs = defaultdict(int)
        for card in hand:
            freqs[card] += 1
        """

        for key in sorted(freqs):
            while freqs[key] > 0:
                freqs[key] -= 1
                for i in range(1, groupSize):
                    if freqs[key + i] > 0:
                        freqs[key + i] -= 1
                    else:
                        return False

        return True

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        groups = [[hand.pop()]]
        print(groups)
        while hand:
            card = hand.pop()
            inserted = False
            for group in groups:
                if len(group) == groupSize and (card < group[0] or card > group[-1]):
                    continue
                if card > group[-1]:
                    group.append(card)
                    inserted = True
                else:
                    l, r = 0, len(group) - 1
                    idx = -1
                    while l <= r:
                        mid = (l + r) // 2
                        if group[mid] > card:
                            idx = mid
                            r -= 1
                        elif group[mid] < card:
                            l += 1
                        else:
                            idx = -1
                            break
                    if idx != -1:
                        if len(group) != groupSize:
                            group.insert(idx, card)                       
                        else:
                            idx -= 1
                            hand.append(group[idx])
                            group[idx] = card
                        inserted = True
                print(idx)
                if inserted:
                    break      
            if not inserted:
                groups.append([card])
            print(card, groups)

        for group in groups:
            if len(group) != groupSize:
                return False
            prev = group[0]
            for i in range(1, groupSize):
                if group[i] != prev + 1:
                    return False
                prev = group[i]

        return True
