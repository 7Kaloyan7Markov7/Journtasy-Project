from random import randint

from background import  Background
from generator import Generator
from asset_manager import AssetManager
from constants import BACKGROUND_IDS


class BackgroundGenerator(Generator):
    def generate(self):
        background_id = BACKGROUND_IDS[randint(0, len(BACKGROUND_IDS))]
        background = Background(background_id)

        return background