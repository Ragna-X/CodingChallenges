def solution(myString):
    return ''.join([char.upper() if char == 'a' else char.lower() if char.isupper() and char != 'A' else char for char in myString])