def solution(my_string):
    tokens = my_string.split(" ")
    current_sign = 1
    answer = []
    for token in tokens :
        if token == "-":
            current_sign = -1
        elif token.isdigit():
            answer.append(int(token) * current_sign) 
            current_sign = 1
    return sum(answer)