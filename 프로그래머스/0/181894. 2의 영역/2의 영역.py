def solution(arr):
    idx_list = [idx for idx, val in enumerate(arr) if val == 2]
    return arr[min(idx_list):max(idx_list) + 1] if idx_list else [-1]