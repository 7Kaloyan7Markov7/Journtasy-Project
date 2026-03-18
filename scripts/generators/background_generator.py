from random import randint

from scripts.building_blocks.background import  Background
from scripts.generators.generator import Generator
from scripts.managers.asset_manager import AssetManager
from scripts.constants.constants import BACKGROUND_IDS


class BackgroundGenerator(Generator):
    def generate(self):
        random_id = BACKGROUND_IDS[randint(0, len(BACKGROUND_IDS) - 1)]
        background = Background(random_id)

        return background