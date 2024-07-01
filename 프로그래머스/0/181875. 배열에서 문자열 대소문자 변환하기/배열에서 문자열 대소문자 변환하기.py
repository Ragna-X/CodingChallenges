def solution(strArr):
    return [char.lower() if idx % 2 == 0 else char.upper() for idx, char in enumerate(strArr)]