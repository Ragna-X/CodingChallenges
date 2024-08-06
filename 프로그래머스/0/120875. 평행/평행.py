from itertools import combinations

def solution(dots):
    def is_parallel(p1, p2, p3, p4):
        dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
        dx2, dy2 = p4[0] - p3[0], p4[1] - p3[1]
        return dy1 * dx2 == dy2 * dx1

    for (p1, p2), (p3, p4) in combinations(combinations(dots, 2), 2):
        if len({tuple(p1), tuple(p2), tuple(p3), tuple(p4)}) == 4:
            if is_parallel(p1, p2, p3, p4):
                return 1
    
    return 0