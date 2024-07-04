def solution(arr):
    row_count = len(arr)
    max_column_count = max(len(row) for row in arr)
    for idx in range(row_count):
        if len(arr[idx]) < row_count:
            arr[idx] = arr[idx] + [0] * (row_count - len(arr[idx]))
    
    if max_column_count> row_count:
        for i in range(max_column_count- row_count):
            arr.append([0] * max_column_count)
    return arr