def solution(chicken):
    total_bonus_chicken = 0
    coupon = chicken
    
    while coupon >= 10:
        coupon_chicken = coupon // 10
        total_bonus_chicken += coupon_chicken
        coupon = coupon % 10 + coupon_chicken
    
    return total_bonus_chicken