def solution(arr):
    count = 0
    while True:
        new_arr = [num / 2 if (50 <= num and num % 2 == 0) else 
                   ( num * 2 + 1 if 50 > num and num % 2 != 0 else num)
                   for num in arr]
        if arr == new_arr:
            break
        count += 1
        arr = new_arr
    return count