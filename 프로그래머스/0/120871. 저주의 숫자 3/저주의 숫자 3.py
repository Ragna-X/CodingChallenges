def solution(n):
    current_number = 1
    valid_count = 1
    while valid_count < n:
        current_number += 1
        if current_number % 3 != 0 and "3" not in str(current_number):
            valid_count += 1
    return current_number