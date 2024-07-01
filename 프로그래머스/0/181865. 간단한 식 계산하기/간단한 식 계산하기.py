def solution(binomial):
    def apply_operation(x, y, opertaion):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
    a, op, b = binomial.split()
    return apply_operation(int(a), int(b), op)