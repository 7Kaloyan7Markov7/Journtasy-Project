from scene import Scene
from asset_manager import AssetManager

class MainMenu(Scene):
    def __init__(self, start_button, quit_button, background):
        self.start_button = start_button
        self.quit_button = quit_button
        self.background = AssetManager.load

    def update():
        pass

    def render():
        pass