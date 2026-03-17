from game_scene import GameScene
from main_menu_scene import MainMenu


class SceneManager:
    def __init__(self):
        self._main_menu = MainMenu()
        self._game_scene = GameScene()
        self._current_scene = self._main_menu

    @property
    def current_scene(self):
        return self._current_scene

    def create_scene(self):
        ...

    def change_scene(self):
        ...

    def update_scene(self):
        self.current_scene.update()

    def render_scene(self, screen):
        self.current_scene.render(screen)