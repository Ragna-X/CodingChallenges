def solution(score):
    average = [(english + math) / 2 for english, math in score]
    indexed_averages = list(enumerate(average))
    sorted_averages = sorted(indexed_averages, key = lambda x : x[1], reverse=True)
    rank = [0] * len(score)
    current_rank = 1
    
    for i, (original_idx, avg) in enumerate(sorted_averages):
        if i > 0 and avg == sorted_averages[i-1][1]:
            rank[original_idx] = rank[sorted_averages[i-1][0]]
        else:
            rank[original_idx] = current_rank
        current_rank += 1
    return rank