import pygame

class Room:
    def __init__(self, background, player, enemies, obstacles):
        self.background = background
        self.player = player
        self.enemies = enemies
        self.obstacles = obstacles

    def render(self, screen):
        screen.blit(self.background, (0,0))
        self.player.render(screen)

        for enemy in self.enemies:
            enemy.render(screen)

        for obstacle in self.obstacles:
            obstacle.render(screen)

    def update():
        pass