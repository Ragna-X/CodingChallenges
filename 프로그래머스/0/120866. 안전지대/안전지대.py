def solution(board):
    n = len(board)
    marked_calls = [[False] * n for _ in range(n)]
    
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    
    for row in range(n):
        for col in range(n):
            if board[row][col]:
                for drow, dcol in directions:
                    mark_row, mark_col = row + drow, col + dcol
                    if 0 <= mark_row < n and 0 <= mark_col < n:
                        marked_calls[mark_row][mark_col] = True
                marked_calls[row][col] = True
                
    total_count = n * n
    marked_count = sum(sum(row) for row in marked_calls)
    return total_count - marked_count