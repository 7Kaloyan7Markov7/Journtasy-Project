from asset_manager import AssetManager
from constants import TOP_LEFT_CORNER

class Background:
    def  __init__(self, background_id):
        self.background_id = background_id
        self.image = AssetManager.get_background(background_id)
    
    def render(self, screen):
        screen.blit(self.image, TOP_LEFT_CORNER)
