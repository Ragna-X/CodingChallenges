def solution(code):
    mode = 0
    answer = []
    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode
        elif (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 != 0):
            answer.append(char)
    return "".join(answer) if answer else "EMPTY"