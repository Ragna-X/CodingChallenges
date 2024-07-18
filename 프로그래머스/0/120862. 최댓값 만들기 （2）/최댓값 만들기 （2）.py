def solution(numbers):
    numbers = sorted(numbers, reverse=True)
    max_product = numbers[0] * numbers[1]
    min_product = numbers[-1] * numbers[-2]
    return max(max_product, min_product)