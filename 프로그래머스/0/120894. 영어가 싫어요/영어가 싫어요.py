def solution(numbers):
    import re
    numbers_by_char = {
        "zero": "0", "one": "1", "two": "2", 
        "three": "3", "four": "4", "five": "5", 
        "six": "6", "seven": "7", "eight": "8", 
        "nine": "9"
    }
    
    pattern = re.compile("|".join(numbers_by_char.keys()))
    numbers = pattern.sub(lambda x : numbers_by_char[x.group()], numbers)
    
    return int(numbers)