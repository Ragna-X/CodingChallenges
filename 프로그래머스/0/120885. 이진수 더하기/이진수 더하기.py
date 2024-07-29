def solution(bin1, bin2):
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    answer = ""
    carry = 0 
    
    for i in range(max_len -1, -1, -1):
        total_sum = int(bin1[i]) + int(bin2[i]) + carry
        carry = total_sum // 2
        answer = str(total_sum % 2) + answer
        
    if carry == 1:
        answer = str(carry) + answer
        
    return answer