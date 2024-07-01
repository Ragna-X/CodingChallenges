def solution(n):
    def create_row(size, row_idx):
        return [1 if row_idx == col_idx else 0 for col_idx in range(size)]
    return [create_row(n, row_idx) for row_idx in range(n)]