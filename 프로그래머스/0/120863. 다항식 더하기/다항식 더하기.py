def solution(polynomial):
    digit_sum, var_sum = 0, 0
    
    for term in polynomial.split(" "):
        if term == "+":
            continue
        elif "x" in term:
            if term == "x":
                var_sum += 1
            else:
                var_sum += int(term.replace("x", ""))
        else:
            digit_sum += int(term)
            
    answer = []
    if var_sum > 0:
        if var_sum == 1:
            answer.append("x")
        else:
            answer.append(f"{var_sum}x")
    if digit_sum > 0:
        answer.append(str(digit_sum))
    return " + ".join(answer)
