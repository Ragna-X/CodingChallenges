def solution(arr, idx):
    for offset, value in enumerate(arr[idx:]):
        if value == 1:
            return offset + idx
    return -1