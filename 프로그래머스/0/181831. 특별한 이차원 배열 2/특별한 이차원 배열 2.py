def solution(arr):
    n = len(arr)
    return 1 if all(1 if arr[i][j] == arr[j][i] else 0 for i in range(n) for j in range(n)) else 0