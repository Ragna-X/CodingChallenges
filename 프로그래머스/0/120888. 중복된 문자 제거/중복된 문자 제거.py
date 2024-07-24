def solution(my_string):
    seen_char = {}
    result_char = []
    for char in my_string:
        if char not in seen_char:
            seen_char[char] = True
            result_char.append(char)
    return "".join(result_char)