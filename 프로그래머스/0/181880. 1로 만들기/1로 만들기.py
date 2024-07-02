def solution(num_list):
    def count_operation(num):
        count = 0
        while num != 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = (num - 1)/2
            count += 1
        return count
    
    return sum(count_operation(num) for num in num_list)