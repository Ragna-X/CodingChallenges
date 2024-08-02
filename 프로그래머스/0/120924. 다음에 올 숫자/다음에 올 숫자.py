def solution(common):
    x1 = common[0]
    x2 = common[1]
    c = x2 - x1
    if x2 + c == common[2]:
        return common[-1] + c
    
    d = x2 // x1
    if x2 * d == common[2]:
        return common[-1] * d