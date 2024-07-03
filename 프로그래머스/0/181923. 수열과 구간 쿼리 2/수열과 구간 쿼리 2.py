def solution(arr, queries):
    result = []
    for s, e, k in queries:
        temp = [arr[i] for i in range(s, e+1) if k < arr[i]]
        result.append(min(temp, default=-1))
    return result
    