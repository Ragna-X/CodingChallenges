def solution(my_string):
    from collections import Counter
    string_counter = Counter(list(my_string))
    answer = [0] * 52
    for char, cnt in string_counter.items():
        if "A" <= char <= "Z": 
            answer[ord(char) - ord("A")] = cnt
        else:
            answer[ord(char) - ord("a") + 26] = cnt
    return answer