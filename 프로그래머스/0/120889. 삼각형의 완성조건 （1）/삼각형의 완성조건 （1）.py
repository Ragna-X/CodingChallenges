def solution(sides):
    max_sides = max(sides)
    return 1 if max_sides < sum(sides) - max_sides else 2