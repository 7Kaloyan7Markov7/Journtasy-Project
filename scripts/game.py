import pygame
from asset_manager import AssetManager
from scene_manager import SceneManager
from input_manager import InputManager


class Game:
    def __init__(self, scene_manager, input_manager, event_handler):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = scene_manager
        self.input_manager = input_manager
        self.event_handler = event_handler

    def main_loop(self):

        while self.running:
            self.update_game()
            self.render_game() 
            self.clock .tick(60)

        pygame.quit()

    def load_game(self):
        ...

    def update_game(self):
        self.input_manager.update()
        self.event_handler.handle(self.scene_manager.current_scene, self.input_manager)
        self.scene_manager.update_scene()

    def render_game(self):
        self.scene_manager.render_scene(self.screen)
        pygame.display.flip()