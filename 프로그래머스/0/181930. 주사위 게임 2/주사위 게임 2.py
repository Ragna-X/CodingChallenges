def solution(a, b, c):
    dice_values = [a, b, c]
    unique_values = set(dice_values)
    
    sum_values = sum(dice_values)
    sum_squares = sum(x**2 for x in dice_values)
    sum_cubes = sum(x**3 for x in dice_values)
    
    if len(unique_values) == 3:
        return sum_values
    elif len(unique_values) == 2:
        return sum_values * sum_squares
    else:
        return sum_values * sum_squares * sum_cubes