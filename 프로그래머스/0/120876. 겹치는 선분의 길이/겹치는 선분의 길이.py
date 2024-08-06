def solution(lines):
    points = [0] * 201
    
    for start, end in lines:
        for i in range(start, end):
            points[i + 100] += 1
    
    overlap = 0
    for point in points:
        if point >= 2:
            overlap += 1
    
    return overlap