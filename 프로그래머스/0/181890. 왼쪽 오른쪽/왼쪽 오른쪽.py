def solution(str_list):
    for idx, char in enumerate(str_list):
        if char in ["l", "r"]:
            return str_list[:idx] if char == 'l' else str_list[idx+1:]
    return []