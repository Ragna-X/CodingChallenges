def solution(progresses, speeds):
    answer = []
    days_to_complete = []
    
    for progress, speed in zip(progresses, speeds):
        work = 100 - progress
        if work % speed == 0:
            days_left = work // speed
        else:
            days_left = (work // speed) + 1
        days_to_complete.append(days_left)
        
    current_max_day = days_to_complete[0]
    count = 1
    
    for i in range(1, len(days_to_complete)):
        if days_to_complete[i] <= current_max_day:
            count += 1
        else:
            answer.append(count)
            current_max_day = days_to_complete[i]
            count = 1
            
    answer.append(count)
    return answer