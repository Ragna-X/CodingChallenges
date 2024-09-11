def solution(prices):
    stack = []
    length = len(prices)
    answer = [0] * length
    
    for i in range(length):
        
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
            
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = length - idx - 1
    
    return answer