from scripts.scenes.game_scene import GameScene
from scripts.scenes.main_menu_scene import MainMenu
from scripts.scenes.character_selection_scene import CharacterSelection
from scripts.config.constants import GAME_SCENE_ID

class SceneManager:
    def __init__(self, screen):
        self._main_menu = MainMenu()
        self._character_selection_scene = CharacterSelection()
        self._screen = screen
        self._game_scene = None
        self._current_scene = self._main_menu

    @property
    def current_scene(self):
        return self._current_scene

    def set_game_scene(self, room):
        self._game_scene = GameScene(room)

    def open_main_menu(self):
        self._current_scene = self._main_menu

    def open_character_selection(self):
        self._character_selection_scene
        self._current_scene = self._character_selection_scene

    def open_game_scene(self):
        if self._game_scene is not None:
            self._current_scene = self._game_scene

    def update_scene(self):
        if self._current_scene.scene_id == GAME_SCENE_ID:
            self._current_scene.update()

    def render_scene(self):
        self._current_scene.render(self._screen)