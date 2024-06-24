def solution(a, b):
    concatenated_sum = int(f"{a}{b}")
    product_sum = 2 * a * b
    return max(concatenated_sum, product_sum)