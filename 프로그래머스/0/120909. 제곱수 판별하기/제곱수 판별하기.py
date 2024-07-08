def solution(n):
    x = n
    y = (x + (n // x)) // 2
    
    while y < x:
        x = y
        y = (x + (n // x)) // 2
    
    return 1 if x ** 2 == n else 2

# def solution(n):
#     import math
#     sqrt_n = int(math.sqrt(n))
#     return 1 if sqrt_n ** 2 == n else 2