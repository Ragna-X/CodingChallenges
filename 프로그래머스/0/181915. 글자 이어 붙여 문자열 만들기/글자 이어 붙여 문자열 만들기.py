def solution(my_string, index_list):
    return ''.join(map(my_string.__getitem__, index_list))