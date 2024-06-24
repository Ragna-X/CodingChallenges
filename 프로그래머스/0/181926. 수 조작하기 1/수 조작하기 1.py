def solution(n, control):
    change_number = {"w": 1, "s": -1, "d": 10, "a": -10}
    return n + sum(map(change_number.get, control))