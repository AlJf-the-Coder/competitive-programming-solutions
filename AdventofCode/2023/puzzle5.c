struct map {
    int dest_start; 
    int src_start; 
    int range
};

struct mapListNode {
    struct map *map;
    struct mapListNode *next;
};

struct seedListNode {
    int seed;
    struct seedListNode *next;
};

long long puzzle5_2(lines):
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
    
    for i in range(0, len(seeds), 2):
        min_seed = 10000000000
        for j in range(seeds[i + 1]):
            seed = seeds[i] + j
            for mep in maps:
                for triple in mep:
                    dest_start, src_start, map_range = list(map(int, triple.split()))
                    if src_start <= seed < src_start + map_range:
                        seed += dest_start - src_start
                        break
            min_seed = min(min_seed, seed)
        seeds[i] = min_seed
    return min(seeds[::2])

with open("puzzle5.txt") as f:
    lines = f.readlines()
printf("%lli\n", puzzle5_2(lines))