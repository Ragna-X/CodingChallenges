def solution(my_string, indices):
    return ''.join([char for idx, char in enumerate(my_string) if idx not in indices])