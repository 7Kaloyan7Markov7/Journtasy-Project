from scene import Scene
from asset_manager import AssetManager
import constants as const


class MainMenu(Scene):
    scene_id = const.MAIN_MENU_ID
    def __init__(self, start_button, quit_button, background):
        self.start_button = start_button
        self.quit_button = quit_button
        self.background = background

    def update(self):
        pass

    def render(self, screen):
        pass