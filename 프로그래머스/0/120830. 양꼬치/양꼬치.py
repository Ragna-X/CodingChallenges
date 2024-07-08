def solution(n, k):
    price_skewer = 12000
    price_drink = 2000
    return price_skewer * n + price_drink * k - (n // 10 * price_drink)