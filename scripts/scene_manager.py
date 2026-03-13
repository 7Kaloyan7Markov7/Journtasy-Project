from game_scene import GameScene
from main_menu_scene import MainMenu


class SceneManager:
    def __init__(self, current_scene):
        self.current_scene = current_scene

    def create_scene(self):
        ...

    def change_scene(self):
        ...

    def update_scene(self):
        self.current_scene.update()

    def render_scene(self):
        self.current_scene.render()

    def pause_switch(self):
        self.is_paused = not self.is_paused