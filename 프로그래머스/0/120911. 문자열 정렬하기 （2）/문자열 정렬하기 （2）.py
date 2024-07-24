def solution(my_string):
    lowercase_string = my_string.lower()
    return "".join(sorted(list(lowercase_string)))