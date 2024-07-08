class Grasshopper:
    def __init__(self, hp):
        self.hp = hp

class Ant:
    def __init__(self, damage):
        self.damage = damage

    def attack(self, target):
        attack_count, target.hp = divmod(target.hp, self.damage)
        return attack_count
    
def solution(hp):
    grasshopper = Grasshopper(hp)
    major_ant = Ant(5)
    soldier_ant = Ant(3)
    worker_ant = Ant(1)

    total_ant_count = 0
    for ant in [major_ant, soldier_ant, worker_ant]:
        total_ant_count += ant.attack(grasshopper)

    return total_ant_count