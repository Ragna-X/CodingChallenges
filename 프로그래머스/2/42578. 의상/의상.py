def solution(clothes):
    clothes_count_by_type = {}
    
    for (_, clothes_type) in clothes:
        if clothes_type in clothes_count_by_type:
            clothes_count_by_type[clothes_type] += 1
        else:
            clothes_count_by_type[clothes_type] = 2
    
    total_combi_count = 1
    for count in clothes_count_by_type.values():
        total_combi_count *= count
    
    return total_combi_count - 1