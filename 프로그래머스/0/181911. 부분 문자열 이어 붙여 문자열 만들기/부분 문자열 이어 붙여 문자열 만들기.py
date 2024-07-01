def solution(my_strings, parts):
    return ''.join([string[start:end+1] for string, (start, end) in zip(my_strings, parts)])