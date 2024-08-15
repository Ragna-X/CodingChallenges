# def solution(participant, completion):
#     from collections import Counter
#     counter_p = Counter(participant)
#     counter_c = Counter(completion)
    
#     incomplete_runner = list((counter_p - counter_c).elements())
#     return incomplete_runner.pop()

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1] 