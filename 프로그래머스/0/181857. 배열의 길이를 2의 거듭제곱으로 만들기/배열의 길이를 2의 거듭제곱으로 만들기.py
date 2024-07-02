def solution(arr):
    min_power = 1 << (len(arr) - 1).bit_length()
    arr.extend([0] * (min_power - len(arr)))  
    return arr