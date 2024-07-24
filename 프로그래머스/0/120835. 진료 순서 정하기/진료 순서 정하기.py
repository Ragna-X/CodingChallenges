def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    rank_dict = {value : rank + 1 for rank, value in enumerate(sorted_emergency)}
    return [rank_dict[i] for i in emergency]