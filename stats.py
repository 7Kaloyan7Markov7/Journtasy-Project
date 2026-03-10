class Stats:
    def __init__(self, max_health, damage, armor, speed, level):
        self.max_health = int(max_health)
        self.current_health = int(max_health)
        self.damage = int(damage)
        self.armor = int(armor)
        self.speed = int(speed)
        self.level = int(level)