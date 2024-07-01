def solution(arr, intervals):
    return [elem for (start, end) in intervals for elem in arr[start:end+1]]