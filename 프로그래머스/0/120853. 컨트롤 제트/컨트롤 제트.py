def solution(s):
    s_array = s.split(" ")
    return sum(int(s_array[idx-1]) * -1 if value == "Z" else int(value) for idx, value in enumerate(s_array))