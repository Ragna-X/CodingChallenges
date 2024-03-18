def solution(array):
    frequency = {}
    for i in array:
        if not i in frequency:
            frequency[i] = 0
        frequency[i] += 1
    
    max_frequency = max(frequency.values())
    
    max_frequency_count = 0
    max_frequency_value = None
    
    for value, value_frequency in frequency.items():
        if value_frequency == max_frequency:
            max_frequency_value = value
            max_frequency_count += 1
    
    if max_frequency_count > 1:
        answer = -1 
    else:
        answer = max_frequency_value

    return answer