def solution(arr, query):
    for idx, i in enumerate(query):
        arr = arr[:i+1] if idx % 2 == 0  else arr[i:] 
    return arr