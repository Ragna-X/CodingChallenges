def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    if denom1 > denom2:
        denom = lcm(denom1, denom2)
    elif denom1 < denom2:
        denom = lcm(denom2, denom1)
    else:
        denom = denom1
    
    answer = [denom/denom1 * numer1 + numer2 * denom/denom2, denom]
    gcd_num = gcd(answer[0], answer[1])
    answer = [answer[0]/gcd_num, answer[1]/gcd_num]
    return answer