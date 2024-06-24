def solution(num_list):
    even_digits = ''.join([str(i) for i in num_list if i % 2 == 0])
    odd_digits = ''.join([str(i) for i in num_list if i % 2 != 0])
    return int(even_digits) + int(odd_digits)
