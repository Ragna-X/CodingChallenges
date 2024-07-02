def solution(strArr): 
    answer = {}
    for string in strArr:
        answer[len(string)] = answer.get(len(string), 0) + 1
    return answer[max(answer, key=answer.get)]