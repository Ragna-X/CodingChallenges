from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counter = Counter(dice)
    count = counter.values()
    keys = list(counter.keys())
    
    if len(count) == 1:
        p = keys[0]
        return 1111 * p
    elif 3 in count:
        p = [i for i, count in counter.items() if count == 3][0]
        q = [i for i, count in counter.items() if count == 1][0]
        return (10 * p + q)**2
    elif 2 in count and len(count) == 2:
        p, q = keys
        return (p + q) * abs(p-q)
    elif 2 in count and len(count) == 3:
        q, r = [i for i, count in counter.items() if count == 1]
        return q * r
    else:
        return min(dice)