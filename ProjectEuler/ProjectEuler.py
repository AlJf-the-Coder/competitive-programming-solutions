from functools import reduce 

def largest_palindrome_product(d):
    pals = []
    big = pow(10, d) - 1
    small = pow(10, d-1)
    for  i in range(big, small - 1, -1):
        for j in range(big, small - 1, -1):
            if str(i*j) == ''.join(list(reversed(str(i*j)))):
                pals.append((i,j,i*j))
    return pals


'''def prime_counts(n):
    counts = dict()
    for i in range(n):
        maxfactor = i**0.5
        j = 2
        count = 0
        if i % j == 0:
            if j not in counts:
                counts[j] = count
            while i % j == 0:
                count +=1
                i = i//j
            if count > count[j]:
                count[j] = count
        j = 3            
        while i > 1 and j <= maxfactor:
            count = 0
            if i % j == 0:
                if j not in counts:
                    counts[j] = count
                while i % j == 0:
                    count +=1
                    i = i//j
                if count > count[j]:
                    count[j] = count
            j += 2
'''       


def prod_from_string(s):
    nums = list(map(int, list(s)))
    return reduce(lambda x,y: x*y, nums, 1)

def largest_adjacent_product(n):
    bigint = ''
    ind = -1
    max_prod = 0
    for _ in range(20):
        bigint += input()
    adjacents = list(filter(lambda x: '0' not in x, [bigint[i:i+13] for i in range(0, 1000-n+1)]))
    print(adjacents)
    for i in range(len(adjacents)):
        prod = prod_from_string(adjacents[i])
        if prod > max_prod:
            max_prod = prod
            ind = i
    return max_prod, adjacents[ind]

max_prod, string = largest_adjacent_product(13)
print(max_prod, string)
    


            
