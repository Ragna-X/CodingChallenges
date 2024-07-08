def solution(price):
    discount_rate = 1
    if 100000 <= price < 300000 :
        discount_rate = 0.95
    elif 300000 <= price < 500000:
        discount_rate = 0.9
    elif 500000 <= price:
        discount_rate = 0.8
    return int(price * discount_rate)