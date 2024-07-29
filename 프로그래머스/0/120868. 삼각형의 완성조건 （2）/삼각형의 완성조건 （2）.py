def solution(sides):
    max_side = max(sides)
    other_side = min(sides)
    return len([i for i in range(1, sum(sides)) if max_side - other_side < i])