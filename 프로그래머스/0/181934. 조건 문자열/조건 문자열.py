def solution(ineq, eq, n, m):
    if eq == "=":
        return 1 if (n >= m if ineq == ">" else n <= m) else 0
    return 1 if (n > m if ineq == ">" else n < m) else 0