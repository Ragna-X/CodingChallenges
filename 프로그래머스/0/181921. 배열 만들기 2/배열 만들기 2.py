def solution(l, r):
    answer = [i for i in range(l, r+1) if set(str(i)).issubset({"0", "5"})]
    return answer if answer else [-1]