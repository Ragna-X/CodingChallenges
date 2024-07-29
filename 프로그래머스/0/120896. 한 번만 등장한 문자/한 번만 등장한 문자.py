def solution(s):
    from collections import Counter
    char_counter = Counter(s)
    unique_chars = [char for char, counter in char_counter.items() if counter == 1]
    return "".join(sorted(unique_chars))