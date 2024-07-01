def solution(n):
    def compute(x, result):
        result.append(x)
        if x == 1:
            return result
        elif x % 2 == 0:
            return compute(x // 2, result)
        else:
            return compute(3 * x + 1, result)
    return compute(n, [])