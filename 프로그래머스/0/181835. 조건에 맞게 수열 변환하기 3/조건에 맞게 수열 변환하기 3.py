def solution(arr, k):
    def compute_value(num, k):
        return num + k if k % 2 == 0 else num * k
    return [compute_value(num, k) for num in arr]