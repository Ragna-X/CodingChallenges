def solution(quiz):
    answer = []
    for equation in quiz:
        expression, expected_result = equation.split(" = ")
        terms = expression.split()
        
        current_sum = 0
        current_sign = 1
        
        for term in terms:
            if term == "+":
                current_sign = 1
            elif term == "-":
                current_sign = -1
            else:
                current_sum += int(term) * current_sign
                
        if current_sum == int(expected_result):
            answer.append("O")
        else:
            answer.append("X")
    return answer