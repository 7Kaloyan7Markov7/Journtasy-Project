from scripts.scenes.game_scene import GameScene
from scripts.scenes.main_menu_scene import MainMenu
from scripts.scenes.character_selection_scene import CharacterSelection


class SceneManager:
    def __init__(self):
        self._main_menu = MainMenu()
        self._game_scene = GameScene()
        self._character_selection_scene = CharacterSelection()
        self._current_scene = self._main_menu

    @property
    def current_scene(self):
        return self._current_scene

    def change_scene(self, new_scene):
        self._current_scene = new_scene

    def update_scene(self):
        self.current_scene.update()

    def render_scene(self, screen):
        self.current_scene.render(screen)