def solution(a, d, included):
    return sum(a + d * idx for idx, flag in enumerate(included) if flag)