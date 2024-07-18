def solution(numbers):
    max1, max2 = float("-inf"), float("-inf")
    for number in numbers:
        if number > max1:
            max1, max2 = number, max1
        elif number > max2:
            max2 = number
    return max1 * max2