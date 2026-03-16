from scene import Scene
from asset_manager import AssetManager
from button import Button
from background_generator import BackgroundGenerator
import constants as const


class MainMenu(Scene):
    scene_id = const.MAIN_MENU_ID
    def __init__(self):
        self.start_button = Button(const.START_BUTTON_TEXT, const.START_BUTTON_ID)
        self.exit_button = Button(const.EXIT_BUTTON_TEXT, const.EXIT_BUTTON_ID)
        self.background = BackgroundGenerator.generate()

    def update(self):
        ...

    def render(self, screen):
        self.start_button.render(screen)
        self.exit_button.render(screen)