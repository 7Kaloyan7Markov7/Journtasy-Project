import pygame

from asset_manager import AssetManager
from scene_manager import SceneManager
from input_manager import InputManager
from event_handler import EventHandler
import constants as const


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.scene_manager = SceneManager()
        self.input_manager = InputManager()
        self.event_handler = EventHandler()

    def main_loop(self):

        self.load_game()
        while self.running:
            self.update_game()
            self.render_game()
            self.clock.tick(const.SIXTY_FPS)

        pygame.quit()

    def load_game(self):
        AssetManager.load()    

    def update_game(self):
        self.input_manager.update()
        self.event_handler.handle(self)
        self.scene_manager.update_scene()

    def render_game(self):
        self.scene_manager.render_scene(self.screen)
        pygame.display.flip()