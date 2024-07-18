

def solution(box, n):
    length, width, height = box
    return (length // n) * (width // n) * (height // n)