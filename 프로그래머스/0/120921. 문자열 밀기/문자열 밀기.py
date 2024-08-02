def solution(A, B):
    if A == B:
        return 0
    
    length = len(A)
    
    for i in range(1, length):
        A = A[-1] + A[:-1]
        if A == B:
            return i
        
    return -1