def solution(a, b):
    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    g = gcd(a, b)
    reduced_denominator = b // g
    
    while reduced_denominator % 2 == 0:
        reduced_denominator //= 2
    while reduced_denominator % 5 == 0:
        reduced_denominator //= 5
    
    return 1 if reduced_denominator == 1 else 2