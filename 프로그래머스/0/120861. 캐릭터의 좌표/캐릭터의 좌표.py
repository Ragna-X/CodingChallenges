def solution(keyinput, board):
    coordinates = {"up": (0,1), "down": (0,-1), "left": (-1,0) , "right": (1,0)}
    current_position = [0, 0]
    max_x, max_y = [i//2 for i in board]
    for cmd in keyinput:
        new_x, new_y = tuple(a + b for a, b in zip(current_position, coordinates[cmd]))
        if -max_x <= new_x <= max_x:
            current_position[0] = new_x
        if -max_y <= new_y <= max_y:
            current_position[1] = new_y
    return current_position