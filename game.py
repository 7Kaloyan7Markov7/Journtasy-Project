import pygame

from scripts.managers.asset_manager import AssetManager
from scripts.managers.scene_manager import SceneManager
from scripts.managers.input_manager import InputManager
from scripts.managers.event_handler_manager import EventHandlerManager
import scripts.config.constants as const


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT))
        pygame.display.set_caption("Journtasy")
        self._clock = pygame.time.Clock()
        self.load_game()
        self._running = True
        self._dungeon_manager = None
        self._scene_manager = SceneManager(self._screen)
        self._input_manager = InputManager()
        self._event_handler_manager = EventHandlerManager()

    @property
    def scene_manager   (self):
        return self._scene_manager
    
    @property
    def input_manager(self):
        return self._input_manager
    
    @property
    def event_handler_manager(self):
        return self._event_handler_manager
    
    @property
    def dungeon_manager(self):
        return self._dungeon_manager
    
    @property
    def event_handler_manager(self):
        return self._event_handler_manager
 
    @property
    def running(self):
        return self._running
    
    @dungeon_manager.setter
    def dungeon_manager(self, dungeon_manager):
        self._dungeon_manager = dungeon_manager
    
    @running.setter
    def running(self, running):
        self._running = running

    def main_loop(self):

        while self._running:
            self.update_game()
            self.render_game()
            self._clock.tick(const.SIXTY_FPS / 2)

        pygame.quit()

    def load_game(self):
        AssetManager.load()    

    def update_game(self):
        self._input_manager.update()
        self._event_handler_manager.handle(self)
        self._scene_manager.update_scene()

    def render_game(self):
        self._scene_manager.render_scene()
        pygame.display.flip()