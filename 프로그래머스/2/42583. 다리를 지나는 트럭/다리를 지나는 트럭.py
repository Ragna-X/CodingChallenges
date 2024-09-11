from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    total_weight_on_bridge = 0
    time = 0
    
    for truck in truck_weights:
        while True:
            time += 1
            
            total_weight_on_bridge -= bridge.popleft()
            
            if total_weight_on_bridge + truck <= weight:
                bridge.append(truck)
                total_weight_on_bridge += truck
                break
            else:
                bridge.append(0)
    time += bridge_length
    return time