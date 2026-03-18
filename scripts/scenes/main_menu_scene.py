from scripts.scenes.scene import Scene
from scripts.building_blocks.button import Button
from scripts.generators.background_generator import BackgroundGenerator
import scripts.constants.constants as const


class MainMenu(Scene):
    scene_id = const.MAIN_MENU_ID
    def __init__(self):
        self._start_button = Button(const.START_BUTTON_TEXT, const.START_BUTTON_ID)
        self._exit_button = Button(const.EXIT_BUTTON_TEXT, const.EXIT_BUTTON_ID)
        self._background = BackgroundGenerator().generate() #generates random background

    @property
    def start_button(self):
        return self._start_button
    
    @property
    def exit_button(self):
        return self._exit_button
    
    @property
    def background(self):
        return self._background
    

    def update(self):
        ...


    def render(self, screen):
        self.background.render(screen)
        self.start_button.render(screen)
        self.exit_button.render(screen)