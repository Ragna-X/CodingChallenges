def solution(q, r, code):
    return "".join(char for idx, char in enumerate(code) if idx % q == r)