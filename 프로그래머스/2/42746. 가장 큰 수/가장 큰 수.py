def solution(numbers):
    number_str = "".join(sorted([str(num) for num in numbers], key=lambda x: x*3, reverse=True))
    
    return number_str if number_str[0] != "0" else "0"