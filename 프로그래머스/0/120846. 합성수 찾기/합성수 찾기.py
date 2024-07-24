def solution(n):
    def get_divisors(num):
        divisors = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:
                    divisors.append(num // i)
        return divisors
        
    return len([i for i in range(1, n+1) if len(get_divisors(i)) >= 3])