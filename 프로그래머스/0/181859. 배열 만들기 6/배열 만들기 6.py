def solution(arr):
    i = 0
    stk = []
    for num in arr:
        if stk and stk[-1] == num:
            stk.pop()
        else:
            stk.append(num)
    
    return stk if stk else [-1]