def solution(myStr):
    answer = [k for i in myStr.split("a") for j in i.split("b") for k in j.split("c") if k]
    return answer if answer else ["EMPTY"]
    