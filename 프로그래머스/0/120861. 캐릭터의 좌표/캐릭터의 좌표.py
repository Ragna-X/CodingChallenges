def solution(keyinput, board):
    coordinates = {"up": (0,1), "down": (0,-1), "left": (-1,0) , "right": (1,0)}
    current_dot = (0, 0)
    max_x, max_y = [i//2 for i in board]
    for cmd in keyinput:
        x, y = tuple(a + b for a, b in zip(current_dot, coordinates[cmd]))
        if max_x < x:
            x = max_x
        elif max_x * -1 > x:
            x = max_x * -1
        if max_y < y:
            y = max_y
        elif max_x * -1 > y:
            y = max_y * -1
        current_dot = (x, y)
    return current_dot