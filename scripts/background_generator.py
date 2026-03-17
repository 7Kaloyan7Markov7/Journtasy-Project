from random import randint

from background import  Background
from generator import Generator
from asset_manager import AssetManager
from constants import BACKGROUND_IDS


class BackgroundGenerator(Generator):
    def generate(self):
        random_id = BACKGROUND_IDS[randint(0, len(BACKGROUND_IDS) - 1)]
        background = Background(random_id)

        return background