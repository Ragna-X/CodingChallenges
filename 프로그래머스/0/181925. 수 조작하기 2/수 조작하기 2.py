def solution(numLog):
    move_map = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    current = numLog[0]
    strlog = '' 
    for num in numLog[1:]:
        move = num - current
        strlog += move_map[move]
        current = num
    return strlog