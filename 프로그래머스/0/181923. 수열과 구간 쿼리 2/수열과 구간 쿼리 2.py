def solution(arr, queries):
    return [min([arr[i] for i in range(s, e+1) if k < arr[i]], default=-1) for s, e, k in queries]
    