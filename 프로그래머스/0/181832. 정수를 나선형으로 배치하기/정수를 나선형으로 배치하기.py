def solution(n):
    answer = [[None] * n for _ in range(n)]
    x, y = 0, 0
    count = 1
    current_direction = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while count <= n * n:
        answer[x][y] = count
        count += 1
        
        next_x, next_y = x + direction[current_direction][0], y + direction[current_direction][1]
        if (0 <= next_x < n) and (0 <= next_y < n) and (answer[next_x][next_y] is None):
            x, y = next_x, next_y
        else:
            current_direction = (current_direction + 1) % 4
            x += direction[current_direction][0]
            y += direction[current_direction][1]
    return answer
        