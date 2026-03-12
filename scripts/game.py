import pygame
from asset_manager import AssetManager
from scene_manager import SceneManager
from input_manager import InputManager


class Game:
    def __init__(self, scene_manager, input_manager):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = scene_manager
        self.input_manager = input_manager

    def main_loop(self):

        while self.running:
            self.input_handler()
            self.update()
            self.render() 
            self.clock .tick(60)

        pygame.quit()

    def input_handler(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def load_game(self):
        ...

    def update_game(self):
        ...

    def render_game(self):
        image = pygame.image.load("assets/background_grass.png").convert_alpha()
        self.screen.blit(image, (0, 0))

game = Game(1,2)
game.main_loop()