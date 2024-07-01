def solution(arr, idx):
    for arr_idx, i in enumerate(arr[idx:]):
        if i == 1:
            return arr_idx + idx
    return -1