def solution(balls, share):
    
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
    total_factorial = factorial(balls)
    selected_factorial = factorial(share)
    remaining_factorial = factorial(balls - share)
    
    return total_factorial // (selected_factorial * remaining_factorial)
