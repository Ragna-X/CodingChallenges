def solution(common):
    x1 = common[0]
    x2 = common[1]
    x3 = common[2]
    c = x2 - x1
    if x2 + c == x3:
        return common[-1] + c
    
    d = x2 // x1
    if x2 * d == x3:
        return common[-1] * d