def solution(arr, flag):
    answer = []
    for value, is_flag in zip(arr, flag):
        if is_flag:
            answer.extend([value] * (value * 2))
        else:
            answer = answer[:-value]
    return answer