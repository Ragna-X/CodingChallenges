def solution(picture, k):
    answer = []
    for row in picture:
        temp = [char * k for char in row]
        answer.extend(["".join(temp)] * k)
    return answer