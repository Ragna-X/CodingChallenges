def solution(arr, k):
    seen = set()
    answer = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            answer.append(num)
        if len(seen) == k:
            break
    return answer + [-1] * (k - len(answer)) if len(answer) < k else answer 