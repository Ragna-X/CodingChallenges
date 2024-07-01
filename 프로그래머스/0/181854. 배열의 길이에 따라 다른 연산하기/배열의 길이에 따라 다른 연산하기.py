def solution(arr, n):
    start_idx = 0 if len(arr) % 2 != 0 else 1
    for i in range(start_idx, len(arr), 2):
        arr[i] += n
    return arr