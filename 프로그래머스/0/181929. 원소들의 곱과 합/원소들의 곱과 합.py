from functools import reduce

def solution(num_list):
    total_sum_squared = sum(num_list)**2
    product = reduce(lambda x, y: x * y, num_list)
    return int(product < total_sum_squared)