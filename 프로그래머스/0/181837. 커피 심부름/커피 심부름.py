def solution(order):
    menu = {"americano": 4500, "cafelatte": 5000}
    default_coffee = "americano"
    
    def calculate_price(coffee):
        if coffee == "anything":
            coffee = default_coffee
        return menu[coffee.replace("hot", "").replace("ice", "").strip()]
    
    return sum(calculate_price(coffee) for coffee in order)