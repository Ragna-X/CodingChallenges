def solution(my_string):
    return sum(map(int, "".join(char if char.isdigit() else " " for char in my_string).split()))