def solution(num, total):
    x = (total - (num - 1) * num // 2) // num
    return [x + i for i in range(0, num)]