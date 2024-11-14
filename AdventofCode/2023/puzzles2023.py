from functools import cmp_to_key 
from math import sqrt, floor
import sys
sys.setrecursionlimit(20000)
def puzzle1_1(lines):
    ret = 0
    for line in lines:
        nums = list(filter(lambda x: x.isdigit(), line))
        ret += int(nums[0] + nums[-1])
    return ret

def puzzle1_2(lines):
    ret = 0
    num_dict = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for line in lines:
        nums = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                nums.append(line[i])
            elif line[i:i+3] in num_dict:
                nums.append(num_dict[line[i:i+3]])
            elif line[i:i+4] in num_dict:
                nums.append(num_dict[line[i:i+4]])
            elif line[i:i+5] in num_dict:
                nums.append(num_dict[line[i:i+5]])
            i += 1
                
        ret += int(nums[0] + nums[-1])
        print(nums[0], nums[-1], line)
    return ret

def puzzle2_1(lines):
    r,g,b = (12, 13, 14) #(r,g,b)
    ret = 0
    for line in lines:
        line = line.split(':')
        game_id = int(line[0].split()[1])
        game = line[1].split(';')
        valid = True
        for pull in game:
            for pair in pull.split(','):
                value, color = pair.split()
                value = int(value)
                if color== 'green' and g < value or color == 'red' and r < value or \
                    color == 'blue' and b < value:
                        valid = False
                if not valid:
                   break
            if not valid:
                break
        if valid:
            ret += game_id
    return ret
                    
def puzzle2_2(lines):
    r,g,b = (12, 13, 14) #(r,g,b)
    ret = 0
    for line in lines:
        line = line.split(':')
        min_r = min_g = min_b = 0
        game = line[1].split(';')
        for pull in game:
            for pair in pull.split(','):
                value, color = pair.split()
                value = int(value)
                if color== 'green' and min_g < value:
                    min_g = value
                elif color == 'red' and min_r < value:
                    min_r = value
                elif color == 'blue' and min_b < value:
                    min_b = value
        ret += min_r*min_g*min_b  
    return ret




def puzzle3_2(lines):
    lines = list(map(lambda x: x.strip(), lines))
    def symbol_near(coords):
        i, j = coords
        j1, j2 = j
        top = lines[i - 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i > 0 else ''
        bot = lines[i + 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i < len(lines) - 1 else ''
        left = lines[i][j1 - 1] if j1 > 0 else ''
        right = lines[i][j2 + 1] if j2 < len(lines[i]) - 1 else ''
        return any(map(lambda x: x != '.' and not x.isdigit(), top + left + right + bot))

    nums = []
    for i in range(len(lines)):
        j1 = 0
        found_num = False
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() and not found_num:
                j1 = j
                found_num = True
            elif not lines[i][j].isdigit() and found_num:
                nums.append((i, (j1, j - 1)))
                found_num = False
        if found_num:
            nums.append((i, (j1, j)))

    return sum(map(lambda x: int(lines[x[0]][x[1][0]: x[1][1] + 1]) if symbol_near(x) else 0, nums))

def puzzle3_1(lines):
    lines = list(map(lambda x: x.strip(), lines))
    def symbol_near(coords):
        i, j = coords
        j1, j2 = j
        top = lines[i - 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i > 0 else ''
        bot = lines[i + 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i < len(lines) - 1 else ''
        left = lines[i][j1 - 1] if j1 > 0 else ''
        right = lines[i][j2 + 1] if j2 < len(lines[i]) - 1 else ''
        return any(map(lambda x: x != '.' and not x.isdigit(), top + left + right + bot))

    nums = []
    for i in range(len(lines)):
        j1 = 0
        found_num = False
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() and not found_num:
                j1 = j
                found_num = True
            elif not lines[i][j].isdigit() and found_num:
                nums.append((i, (j1, j - 1)))
                found_num = False
        if found_num:
            nums.append((i, (j1, j)))

    return sum(map(lambda x: int(lines[x[0]][x[1][0]: x[1][1] + 1]) if symbol_near(x) else 0, nums))

def puzzle3_2(lines):
    lines = list(map(lambda x: x.strip(), lines))
    out = 0
    def symbol_near(coords):
        i, j = coords
        j1, j2 = j
        top = lines[i - 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i > 0 else ''
        bot = lines[i + 1][max(j1 - 1, 0): min(len(lines[i]) , j2 + 2)] if i < len(lines) - 1 else ''
        left = lines[i][j1 - 1] if j1 > 0 else ''
        right = lines[i][j2 + 1] if j2 < len(lines[i]) - 1 else ''
        return any(map(lambda x: x != '.' and not x.isdigit(), top + left + right + bot))

    nums = []
    for i in range(len(lines)):
        j1 = 0
        found_num = False
        for j in range(len(lines[i])):
            if lines[i][j].isdigit() and not found_num:
                j1 = j
                found_num = True
            elif not lines[i][j].isdigit() and found_num:
                nums.append((i, (j1, j - 1)))
                found_num = False
        if found_num:
            nums.append((i, (j1, j)))

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                fits = list(filter(lambda x: abs(x[0] - i) <= 1 and x[1][0] - 1 <=  j <= x[1][1] + 1, nums))
                if len(fits) == 2:
                    fits = list(map(lambda x: int(lines[x[0]][x[1][0]: x[1][1] + 1]), fits))
                    out += fits[0] * fits[1]

    return out

def puzzle4_1(lines):
    lines = list(map(lambda x: x.strip(), lines))
    out = 0
    for line in lines:
        line = line.split(': ')[1]
        winning, chosen = line.split(' | ')
        winning = winning.split()
        chosen = chosen.split()
        right = len(list(filter(lambda x: x in winning, chosen)))
        out += 2**(right - 1) if right > 0 else 0
    return out

def puzzle4_2(lines):
    lines = list(map(lambda x: x.strip(), lines))
    card_copies = [0 for _ in range(len(lines))]
    out = 0
    for i in range(len(lines)):
        line = lines[i].split(': ')[1]
        winning, chosen = line.split(' | ')
        winning = winning.split()
        chosen = chosen.split()
        right = len(list(filter(lambda x: x in winning, chosen)))
        for j in range(i+1, min(len(lines), i + right + 1)):
            card_copies[j] += 1 + card_copies[i]
    return len(lines) + sum(card_copies)

def puzzle5_1(lines):
    def split_by(lst, item):
        ret = []
        list_copy = list(lst)
        while list_copy.count(item) > 0:
            ind = list_copy.index(item)
            app, list_copy = list_copy[:ind], list_copy[ind+1:]
            ret.append(app)
        if len(list_copy) > 0:
            ret.append(list_copy)
        return ret

    lines = list(map(lambda x: x.strip(), lines))
    lines = split_by(lines, '')
    seeds, maps = lines[0][0], lines[1:]
    seeds = list(map(int, seeds.split(': ')[1].split()))
    maps = list(map(lambda x: x[1:], maps))
    
    for i in range(len(seeds)):
        for mep in maps:
            for triple in mep:
                dest_start, src_start, map_range = list(map(int, triple.split()))
                if src_start <= seeds[i] < src_start + map_range:
                    seeds[i] += dest_start - src_start
                    break
    return min(seeds)

def puzzle5_2(lines):
    def split_by(lst, item):
        ret = []
        list_copy = list(lst)
        while list_copy.count(item) > 0:
            ind = list_copy.index(item)
            app, list_copy = list_copy[:ind], list_copy[ind+1:]
            ret.append(app)
        if len(list_copy) > 0:
            ret.append(list_copy)
        return ret
    
    def range_splitter(seed, spread, i):
        nonlocal min_seed
        if i == 0:
            min_seed = min(min_seed, seed)
            return
        while spread > 0:
            next_src_start = maps[i][0][1]
            offset = next_src_start - seed
            # check if number lower than lowest number in map
            if offset > 0:
                range_splitter(seed, min(spread, offset), i + 1)
                seed += min(spread, offset)
                spread -= min(spread, offset)
            if spread <= 0:
                break
            for j in range(len(maps[i])):
                triple = maps[i][j]
                dest_start, src_start, map_range = triple
                if src_start <= seed < src_start + map_range:
                    # check if number in range
                    offset = seed - src_start 
                    range_splitter(seed + dest_start - src_start, min(spread, map_range - offset), i + 1)
                    seed += min(spread, map_range - offset)
                    spread -= min(spread, map_range - offset)
                    if spread <= 0:
                        break
                if j < len(maps[i]) - 1:
                    # see if starts in next range else use up numbers before the next range
                    next_src_start = maps[i][j + 1][1]
                    offset = next_src_start - seed
                    if offset > 0:
                        range_splitter(seed, min(spread, offset), i + 1)
                        seed += min(spread, offset)
                        spread -= min(spread, offset)
                if spread <= 0:
                    break
            if spread > 0:
                # numbers greater than specified ranges in map
                range_splitter(seed, spread, i + 1)
                spread = 0
        

    lines = list(map(lambda x: x.strip(), lines))
    lines = split_by(lines, '')
    seeds, maps = lines[0][0], lines[1:]
    seeds = list(map(int, seeds.split(': ')[1].split()))
    maps = list(map(lambda x: x[1:], maps))
    maps = list(map(lambda x: list(map(lambda y: [int(x) for x in y.split()], x)), maps))
    for i in range(len(maps)):
        maps[i].sort(key = lambda x: x[1])
    min_seed = 10000000000
    for i in range(0, len(seeds), 2):
        range_splitter(seeds[i], seeds[i+1], -len(maps))
    return min_seed

def puzzle6_1(lines):
    time = list(map(int, lines[0].split(':')[1].split()))
    dists = list(map(int, lines[1].split(':')[1].split()))
    ret = 1
    for i in range(len(time)):
        count = 0
        for j in range(time[i]):
            if (time[i] - j) * j > dists[i]:
                count += 1
            elif j > time[i] / 2 and (time[i] - j) * j < dists[i]:
                break
        ret *= count
    return ret

def puzzle6_2(lines):
    time = int(''.join(lines[0].split(':')[1].split()))
    dist = int(''.join(lines[1].split(':')[1].split()))
    count = 0
    for i in range(time):
        if (time - i) * i > dist:
            count += 1
        elif i > time / 2 and (time - i) * i < dist:
            break
    return count

def puzzle7_1(lines):
    def classify_hand(cards):
        ucards = list(set(cards))
        counts = list(map(lambda x: cards.count(x), ucards))
        counts = list(map(lambda x: counts.count(x), range(6)))

        if counts[5] == 1:
            hand_type = 6 #five of a kind
        elif counts[4] == 1:
            hand_type = 5 #four of a kind
        elif counts[3] == 1 and counts[2] == 1:
            hand_type = 4 #full house
        elif counts[3] == 1 and counts[1] == 2:
            hand_type = 3 #three of a kind
        elif counts[2] == 2 and counts[1] == 1:
            hand_type = 2 #two pair
        elif counts[2] == 1 and counts[1] == 3: 
            hand_type = 1 #one pair
        else:
            hand_type = 0 #high card 
        return hand_type
    
    def compare_cards(cards1, cards2):
        hand1 = classify_hand(cards1)
        hand2 = classify_hand(cards2)
        if hand1 > hand2:
            return 1
        elif hand2 > hand1:
            return -1
        else:
            for card1, card2 in zip(cards1, cards2):
                if card1 > card2:
                    return 1
                elif card2 > card1:
                    return -1
            return 0

    def convert_to_nums(cards):
        for i in range(5):
            match cards[i]:
                case 'A':
                    cards[i] = 12
                case 'K':
                    cards[i] = 11
                case 'Q':
                    cards[i] = 10
                case 'J':
                    cards[i] = 9
                case 'T':
                    cards[i] = 8
                case _:
                    cards[i] = int(cards[i]) - 2
        return cards


    
        
    lines = list(map(lambda x: x.strip().split(), lines))
    cards, bids = list(map(lambda x: x[0], lines)), list(map(lambda x: x[1], lines))
    cards = list(map(lambda x: convert_to_nums(list(x)), cards))
    bids = list(map(int, bids))
    hands_bids = list(zip(cards, bids))
    ret = 0
    hands_bids.sort(key = lambda x: cmp_to_key(compare_cards)(x[0]))
    for hand, bid in hands_bids:
        print(hand, classify_hand(hand), bid)
    for i, (_, bid) in enumerate(hands_bids, start = 1):
        ret += i * bid
    return ret

def puzzle7_2(lines):
    def classify_hand(cards):
        ucards = list(set(cards))
        counts = list(map(lambda x: cards.count(x), ucards))
        counts = list(map(lambda x: counts.count(x), range(6)))
        j_count = cards.count(0)

        if counts[5] == 1 or j_count == 1 and counts[4] == 1 or j_count == 2 and counts[3] == 1\
            or j_count == 3 and counts[2] == 1 or j_count == 4:
            hand_type = 6 #five of a kind
        elif counts[4] == 1 or j_count == 1 and counts[3] == 1\
            or j_count == 2 and counts[2] == 2 or j_count == 3 and counts[1] == 2:
            hand_type = 5 #four of a kind
        elif counts[3] == 1 and counts[2] == 1 or j_count == 1 and counts[2] == 2:
            hand_type = 4 #full house
        elif counts[3] == 1 and counts[1] == 2 or j_count == 1 and counts[2] == 1\
            or j_count == 2 and counts[1] == 3:
            hand_type = 3 #three of a kind
        elif counts[2] == 2 and counts[1] == 1:
            hand_type = 2 #two pair
        elif counts[2] == 1 and counts[1] == 3 or j_count == 1 and counts[1] == 5: 
            hand_type = 1 #one pair
        else:
            hand_type = 0 #high card 
        return hand_type
    
    def compare_cards(cards1, cards2):
        hand1 = classify_hand(cards1)
        hand2 = classify_hand(cards2)
        if hand1 > hand2:
            return 1
        elif hand2 > hand1:
            return -1
        else:
            for card1, card2 in zip(cards1, cards2):
                if card1 > card2:
                    return 1
                elif card2 > card1:
                    return -1
            return 0

    def convert_to_nums(cards):
        for i in range(5):
            match cards[i]:
                case 'A':
                    cards[i] = 12
                case 'K':
                    cards[i] = 11
                case 'Q':
                    cards[i] = 10
                case 'T':
                    cards[i] = 9
                case 'J':
                    cards[i] = 0
                case _:
                    cards[i] = int(cards[i]) - 1
        return cards


    
        
    lines = list(map(lambda x: x.strip().split(), lines))
    cards, bids = list(map(lambda x: x[0], lines)), list(map(lambda x: x[1], lines))
    cards = list(map(lambda x: convert_to_nums(list(x)), cards))
    bids = list(map(int, bids))
    hands_bids = list(zip(cards, bids))
    ret = 0
    hands_bids.sort(key = lambda x: cmp_to_key(compare_cards)(x[0]))
    for hand, bid in hands_bids:
        print(hand, classify_hand(hand), bid)
    for i, (_, bid) in enumerate(hands_bids, start = 1):
        ret += i * bid
    return ret

def puzzle8_1(lines):
    locations = dict()
    lines = list(map(lambda x: x.strip(), lines))
    directions, lines = lines[0], lines[2:]
    directions = list(map(lambda x: 1 if x == "R" else 0, directions))
    for line in lines:
        key, val = line.split(" = ")
        val = val.rstrip(")").lstrip("(").split(', ')
        locations.update({key: val})
    current = 'AAA'
    steps = 0
    while current != 'ZZZ':
        for dir in directions:
            current = locations[current][dir]
            steps += 1
            if current == 'ZZZ':
                break

    return steps

def puzzle8_2(lines):
    locations = dict()
    lines = list(map(lambda x: x.strip(), lines))
    directions, lines = lines[0], lines[2:]
    directions = list(map(lambda x: 1 if x == "R" else 0, directions))
    for line in lines:
        key, val = line.split(" = ")
        val = val.rstrip(")").lstrip("(").split(', ')
        locations.update({key: val})
    currents = list(filter(lambda x: x[-1] == 'A', locations.keys()))
    for i in range(len(currents)):
        current = currents[i]
        steps = 0
        while current[-1] != 'Z':
            for dir in directions:
                current = locations[current][dir]
                steps += 1
                if current[-1] == 'Z':
                    break
        currents[i] = steps
    primes = prime_factors_list(currents)
    print(currents)
    ret = 1
    for key in primes.keys():
        ret *= key**primes[key]
    return ret

def is_prime(num):
    if num < 2: return False
    if num == 2 or num == 3: return True
    if num % 2 == 0: return False
    if num % 3 == 0: return False
    for i in range(3, floor((sqrt(num))) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_factors(num):
    factors = dict()
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            count = 0
            while num % i == 0:
                num = num / i
                count += 1
            factors.update({i: count})
    return factors

def prime_factors_list(nums):
    '''returns the prime_factors of a list of numbers and the multiplicity for an evenly divisible number'''
    factors = dict()
    for num in nums:
        num_factors = prime_factors(num)
        for key in num_factors:
            if key not in factors or num_factors[key] > factors[key]: 
                factors.update({key: num_factors[key]})
    return factors

def puzzle9_1(lines):
    
    lines = list(map(lambda x: x.strip().split(), lines))
    ret = 0
    for line in lines:
        sequence = list(map(int, line))
        lasts = [sequence[-1]]
        while any(map(lambda x: x != 0, sequence)):
            sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
            lasts.append(sequence[-1])

        for i in range(-2, -len(lasts) - 1, -1):
            lasts[i] = lasts[i + 1] + lasts[i]
        print(lasts[0])
        ret += lasts[0]
    return ret

def puzzle9_2(lines):
    lines = list(map(lambda x: x.strip().split(), lines))
    ret = 0
    for line in lines:
        sequence = list(map(int, line))
        firsts = [sequence[0]]
        while any(map(lambda x: x != 0, sequence)):
            sequence = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
            firsts.append(sequence[0])

        for i in range(-2, -len(firsts) - 1, -1):
            firsts[i] = firsts[i] - firsts[i + 1]
        print(firsts[0])
        ret += firsts[0]
    return ret

def puzzle10_1(lines):
    def traverse_maze(y, x, pdir):
        #check if in bounds
        if y >= len(lines) or y < 0 or x >= len(lines[y]) or x < 0:
            return
        
        pipe = lines[y][x]

        #pipes that can be entered/exited from a specific direction
        up = '|LJ' 
        down = '|7F'
        left = '-J7'
        right = '-LF'

        #check if entered appropriate pipe
        match pdir:
            case 'up':
                if pipe == 'S':
                    if start_dir == "down":
                        lines[s[0]][s[1]] = '|'
                        return 1, [(y,x)]
                    elif start_dir == "left":
                        lines[s[0]][s[1]] = 'J'
                        return 1, [(y,x)]
                    elif start_dir == "right":
                        lines[s[0]][s[1]] = 'L'
                        return 1, [(y,x)]
                if pipe not in up: 
                    return -1, []
            case 'down':
                if pipe == 'S':
                    if start_dir == "up":
                        lines[s[0]][s[1]] = '|'
                        return 1, [(y,x)]
                    elif start_dir == "left":
                        lines[s[0]][s[1]] = '7'
                        return 1, [(y,x)]
                    elif start_dir == "right":
                        lines[s[0]][s[1]] = 'F'
                        return 1, [(y,x)]
                if pipe not in down:
                    return -1, []
            case 'right':
                if pipe == 'S':
                    if start_dir == "up":
                        lines[s[0]][s[1]] = 'L'
                        return 1, [(y,x)]
                    elif start_dir == "down":
                        lines[s[0]][s[1]] = 'F'
                        return 1, [(y,x)]
                    elif start_dir == "left":
                        lines[s[0]][s[1]] = '-'
                        return 1, [(y,x)]
                if pipe not in right: 
                    return -1, []
            case 'left':
                if pipe == 'S':
                    if start_dir == "up":
                        lines[s[0]][s[1]] = 'J'
                        return 1, [(y,x)]
                    elif start_dir == "down":
                        lines[s[0]][s[1]] = '7'
                        return 1, [(y,x)]
                    elif start_dir == "right":
                        lines[s[0]][s[1]] = '-'
                        return 1, [(y,x)]
                if pipe not in left:
                    return -1, []


        #choose which direction to go next depending on current pipe (guaranteed to be pipe)
        if pdir != 'up' and pipe in up:
            res = traverse_maze(y - 1, x, 'down')
            if res[0] == 1:
                return res[0], [(y, x)] + res[1]
        if pdir != 'down' and pipe in down:
            res = traverse_maze(y + 1, x, 'up')
            if res[0] == 1:
                return res[0], [(y, x)] + res[1]
        if pdir != 'left' and pipe in left:
            res = traverse_maze(y, x - 1, 'right')
            if res[0] == 1:
                return res[0], [(y, x)] + res[1]
        if pdir != 'right' and pipe in right:
            res = traverse_maze(y, x + 1, 'left')
            if res[0] == 1:
                return res[0], [(y, x)] + res[1]


    lines = list(map(lambda x: list(x.strip()), lines))
    #find s
    s = (-1,-1)
    for i in range(len(lines)): 
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                s = (i, j)
                break
    if s == (-1,-1):
        return -1, []
    
    #traverse maze from all pipes connected to S
    #go up
    if s[0] - 1 >= 0:
        start_dir = "up"
        res = traverse_maze(s[0] - 1, s[1], "down")
        if res[0] == 1:
            return (len(res[1])) // 2, res[1]
    #go down
    if s[0] + 1 < len(lines):
        start_dir = "down"
        res = traverse_maze(s[0] + 1, s[1], "up")
        if res[0] == 1:
            return (len(res[1])) // 2, res[1]
    #go left
    if s[1] - 1 >= 0:
        start_dir = "left"
        res = traverse_maze(s[0], s[1] - 1, "right")
        if res[0] == 1:
            return (len(res[1])) // 2, res[1]
    #go right
    if s[1] + 1 < len(lines[s[0]]):
        start_dir = "right"
        res = traverse_maze(s[0], s[1] + 1, "left")
        if res[0] == 1:
            return (len(res[1])) // 2, res[1]
    return -1, []

def puzzle10_2(lines):
    _, loop_parts = puzzle10_1(lines)
    lines = list(map(lambda x: list(x.strip()), lines))
    indices = [(i,j) for i in range(len(lines)) for j in range(len(lines[i]))]
    inner_parts = []
    for i in range(len(loop_parts)):
        #add and filter
        inner_parts = []
    return len(inner_parts), inner_parts

def puzzle11_1(lines):
    lines = [x.strip() for x in lines] 
    empty_rows = [i for i in range(len(lines)) if '#' not in lines[i]]
    empty_cols = []
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == '#':
                break

        if lines[i][j] != '#':
            empty_cols.append(j)
    
    locations = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                locations.append((i,j))
    
    dists = []
    for i in range(len(locations)):
        for other in locations[i+1:]:
            dist = 0
            #add empty rows
            dist += len([r for r in empty_rows if locations[i][0] < r < other[0]])
            #add empty cols
            dist += len([c for c in empty_cols if min(locations[i][1], other[1]) < c < max(locations[i][1], other[1])])
            #add x distance
            dist += abs(locations[i][0] - other[0])
            #add y distance
            dist += abs(locations[i][1] - other[1])
            dists.append(dist)

    return dists, sum(dists)
        
def puzzle11_2(lines, exp_rate = 2):
    lines = [x.strip() for x in lines] 
    empty_rows = [i for i in range(len(lines)) if '#' not in lines[i]]
    empty_cols = []
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] == '#':
                break

        if lines[i][j] != '#':
            empty_cols.append(j)
    
    locations = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                locations.append((i,j))
    
    dists = []
    for i in range(len(locations)):
        for other in locations[i+1:]:
            dist = 0
            #add empty rows
            dist += len([r for r in empty_rows if locations[i][0] < r < other[0]]) * (exp_rate - 1)
            #add empty cols
            dist += len([c for c in empty_cols if min(locations[i][1], other[1]) < c < max(locations[i][1], other[1])]) * (exp_rate - 1)
            #add x distance
            dist += abs(locations[i][0] - other[0])
            #add y distance
            dist += abs(locations[i][1] - other[1])
            dists.append(dist)

    return dists, sum(dists)    
    
def puzzle12_1(lines):
    lines = [x.strip().split() for x in lines]
    combinations = 0
    for seq, groups in lines:
        #calculate
        combinations += 0 #something
    return combinations
     
    
    
    
    
with open("f:/Users/Asus/Documents/Coding_Projects/AdventofCode/puzzle10.txt") as f:
    lines = f.readlines()

print(puzzle10_2(lines))
    
