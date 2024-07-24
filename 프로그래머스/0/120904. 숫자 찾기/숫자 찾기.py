def solution(num, k):
    numbers_str = str(num)
    digit_str = str(k)
    position = numbers_str.find(digit_str)
    return position + 1 if position != -1 else -1